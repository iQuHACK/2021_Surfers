import dimod
import numpy as np

from dwave.system import LeapHybridSampler
from pyqubo import Array, Binary, Placeholder


# +
def solve(
    N, # Number of data points
    K, # Number of clusters
    dist_matrix, # NxN matrix with distances between data points
    gamma_distinct=None, # Coefficent for the penalty of being
    gamma_multiple=None, # Coefficient for the penalty of being assigned to multiple clusters (illegal); should be very high 
    target_goal=None, # Target equal value for each cluster; by default, it's N//K
    point_weights=None,  # N-element Weight Vector for the points in the equal size constraint; by default , we assume all ones
):
    if target_goal is None:
        target_goal = N//K
    
    if point_weights is None:
        point_weights = np.ones(N)
    
    if gamma_distinct is None:
        gamma_distinct = np.max(dist_matrix)
    
    if gamma_multiple is None:
        gamma_multiple = np.max(dist_matrix) # weight bigger than sum of all distances, not worth taking more than one

    group_matrix = Array.create('x', shape=(N, K), vartype='BINARY')

    distinct_size_penalty = Placeholder("gamma_distinct")
    multiple_assignment_penalty = Placeholder("gamma_multiple")
    target = Placeholder("target_goal")

    all_terms = []

    # Penalty for being assigned to multiple clusters
    for i in range(N):
        single_asignment_constraint = (1 - sum(group_matrix[i,:]))**2
        all_terms.append(
            multiple_assignment_penalty*single_asignment_constraint
        )

    # Penalty for exceding equal number of members per cluster
    for j in range(K):
        cluster_member_constraint = (target - sum(point_weights*group_matrix[:, j]))**2
        all_terms.append(
            distinct_size_penalty*cluster_member_constraint
        )

    # Adding objective for distances. Must minimize distances in the same group
    for i in range(N):
        for j in range(i+1, N):
            same_group_combinations = group_matrix[i,:] * group_matrix[j,:]
            all_terms.append(
                dist_matrix[i,j] * sum(same_group_combinations)
            )

    # Generate QUBO from equation that represents the DQM
    equation = sum(all_terms)
    model = equation.compile()
    Q, offset = model.to_qubo(
        feed_dict={
            'gamma_distinct': gamma_distinct, "gamma_multiple": gamma_multiple, "target_goal": target_goal
        }
    )

    # Call D-Wave solver
    sampler = LeapHybridSampler()

    answer = sampler.sample_qubo(Q)

    best_answer = list(answer.data(['sample', 'energy']))[0].sample

    # Utility function to map from QUBO temp matrix label to integer
    def matrix_entry_to_pair(val):
        _, i, j = val.replace("[", " ").replace("]", " ").split()
        return (int(i), int(j))

    cluster_result = [
        matrix_entry_to_pair(k) for k, v in best_answer.items() if v == 1
    ]

    label_result = [p[1] for p in sorted(cluster_result)]

    return label_result
