#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

"""
Write function blob_classification() that gets feature matrix 'X' and label vector
'y' as parameters. It should then return the accuracy score of the prediction.

Do the prediction using GaussianNB, and use train_test_split() function from sklearn
to split the dataset in to two parts: one for training and one for testing. Give
parameter random_state=0 to the splitting function so that the result is deterministic.

Use training set size of 75% of the whole data.
"""

def blob_classification(X, y):
    TEST = 0.25
    TRAINING = 0.75

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = TEST, train_size = TRAINING, random_state = 0)

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)

    accuracy_score = metrics.accuracy_score(y_test, y_fitted)

    return accuracy_score

def main():
    X,y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)
    print("The accuracy score is", blob_classification(X, y))
    a=np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs=[]
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers=int(row[1]),
                                  random_state=int(row[2]), cluster_std=row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()
