import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

if __name__ == "__main__":
    """
       generate k clusters,
    """
    centers = [[1, 1], [-1, -1], [1, -1]]
    sz_per_cluster = 10
    ft_dim = 2
    stddev = 0.3
    output_name = "tmp"
    n_samples = len(centers) * sz_per_cluster
    x, labels= make_blobs(
            n_samples=n_samples,
            n_features=ft_dim,
            centers=centers,
            cluster_std=stddev)

    df = pd.DataFrame(x, columns=[f"ft_{i}" for i in range(ft_dim)])
    df['label']=labels
    # print(df)
    # print(df.iloc[2,:2].to_numpy())
    df.to_csv(output_name+".csv", index=False)

    plt.scatter(x[:,0], x[:,1], c=labels)
    plt.savefig(output_name+".png", dpi=300)



