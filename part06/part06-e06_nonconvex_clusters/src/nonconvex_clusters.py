#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

"""
Read the tab separated file data.tsv from the src folder into a DataFrame. The dataset has two
features 'X1' and 'X2', and the label 'y'. Cluster the feature matrix using DBSCAN with different
values for the 'eps' parameter. Use values in np.arange(0.05, 0.2, 0.05) for clustering. For each
clustering, collect the accuracy score, the number of clusters, and the number of outliers. Return
these values in a DataFrame, where columns and column names are as in the below example.

     eps   Score  Clusters  Outliers                             
0    0.05      ?         ?         ?1    0.10      ?
?         ?2    0.15      ?         ?         ?3
0.20      ?         ?         ?

Note that DBSCAN uses label -1 to denote outliers, that is, those data points that didn't fit well
in any cluster. You have to modify the find_permutation function to handle this: ignore the outlier
data points from the accuracy score computation. In addition, if the number of clusters is not the
same as the number of labels in the original data, set the accuracy score to NaN.
"""

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]

    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)

    return permutation

def nonconvex_clusters():
    data_frame = pd.read_csv("src/data.tsv",sep="\t")
    X = data_frame[["X1","X2"]]
    y = data_frame["y"]

    eps_values = np.arange(0.05,0.2,0.05)
    label_count = len(y.unique())
    columns = ["eps", "Score", "Clusters", "Outliers"]

    result_array = []

    for eps in eps_values:
        model = DBSCAN(eps=eps)
        model.fit(X)

        labels = model.labels_

        cluster_count = len(set(labels)) - (1 if -1 in labels else 0)
        outlier_count = np.count_nonzero(labels == -1)
        non_outliers = labels != -1

        permutation = find_permutation(cluster_count, y[non_outliers], labels[non_outliers])
        new_labels = [permutation[label] for label in labels[non_outliers]]

        if cluster_count != label_count:
            acc_score = np.nan
        else:
            acc_score = accuracy_score(y[non_outliers], new_labels)

        result_array.append([eps, acc_score, cluster_count, outlier_count])

    return pd.DataFrame(data = result_array,columns = columns, dtype = "float")


def main():
    NC_clusters = nonconvex_clusters()
    print(NC_clusters)

if __name__ == "__main__":
    main()
