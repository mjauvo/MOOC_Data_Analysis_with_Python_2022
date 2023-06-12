#!/usr/bin/env python3

import scipy

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn import metrics

"""
Using the same iris data set that you saw earlier in the classification, apply k-means
clustering with 3 clusters. Create a function plant_clustering that loads the iris data
set, clusters the data and returns the accuracy_score.
"""

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    dataset = load_iris()
    X = dataset.data
    y = dataset.target

    CLUSTERS = 3

    model = KMeans(CLUSTERS, random_state = 0)
    model.fit(X)

    permutation = find_permutation(CLUSTERS, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    accuracy_score = metrics.accuracy_score(y, new_labels)

    return accuracy_score

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
