import numpy as np
import pandas as pd
import dimod
from dwave.system import LeapHybridDQMSampler


data_file = "tmp.csv"
df = pd.read_csv(data_file)
colors = df["label"].unique()
num_colors = colors.shape[0]
num_points = len(df)

dqm = dimod.DiscreteQuadraticModel()

for idx in range(num_points):
    dqm.add_variable(num_colors, label=idx)

def get_distance(i, j, df, num_colors):
    x = df.iloc[i, :num_colors].to_numpy()
    y = df.iloc[j, :num_colors].to_numpy()
    return np.linalg.norm(x-y)

for i in range(num_points):
    for j in range(num_points):
        if i != j:
            energy = get_distance(i, j, df, num_colors=num_colors)
            dqm.set_quadratic(i, j, {(c, c): energy for c in colors})

sampler = LeapHybridDQMSampler()
sampleset = sampler.sample_dqm(dqm)
sample = sampleset.first.sample
energy = sampleset.first.energy
print(f"Energy: {energy}\nSolution: {sample}")

print(f"compare solutions with ground truth")
for i in range(num_points):
    print(sample[i], df["label"][i])
