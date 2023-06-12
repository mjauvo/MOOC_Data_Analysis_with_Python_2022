#!/usr/bin/env python3

import gzip
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

"""
In the 'src' folder there are two files:
- ham.txt.gz
- spam.txt.gz

The files are preprocessed versions of the files from https://spamassassin.apache.org/old/publiccorpus/.
There is one emails per line. The file ham.txt.gz contains emailss that are non-spam, and, conversely, emailss
in file spam.txt are spam. The emails headers have been removed, except for the subject line, and non-ascii
characters have been deleted.

Write function spam_detection() that does the following:

- Reads the lines from these files into arrays. Use function open() from gzip module, since the files are
  compressed. From each file take only fraction of lines from the start of the file, where fraction is a
  parameter to spam_detection(), and should be in the range [0.0, 1.0].
- Forms the combined feature matrix using CountVectorizer class' fit_transform() method. The feature matrix
  should first have the rows for the 'ham' dataset and then the rows for the 'spam' dataset. One row in the
  feature matrix corresponds to one emails.
- Uses labels '0' for ham and '1' for spam
- Divides that feature matrix and the target label into training and test sets, using train_test_split. Use
  75% of the data for training. Pass the random_state parameter from spam_detection to train_test_split.
- Train a MultinomialNB model, and use it to predict the labels for the test set

The function should return a triple consisting of
- accuracy score of the prediction
- size of test sample
- number of misclassified sample points

Note:
The tests use the 'fraction' parameter with value 0.1 to ease to load on the TMC server. If full data were used
and the solution did something non-optimal, it could use huge amounts of memory, causing the solution to fail.
"""

def get_file_content(gz_file, fraction):
    gz_file_lines = gzip.open(gz_file).readlines()
    content_length = int(fraction * len(gz_file_lines))
    content = gz_file_lines[:content_length]

    return content

def spam_detection(random_state=0, fraction=1.0):
    ham = get_file_content("src/ham.txt.gz", fraction)
    spam = get_file_content("src/spam.txt.gz", fraction)
    labels_ham = np.zeros(len(ham))
    labels_spam = np.ones(len(spam))

    emails = ham + spam
 
    TEST = 0.25
    TRAINING = 0.75

    CV = CountVectorizer()

    X = CV.fit_transform(emails).toarray()
    y = np.concatenate((labels_ham, labels_spam))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = TEST, train_size = TRAINING, random_state = random_state)
    
    model = MultinomialNB()

    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)

    accuracy_score = metrics.accuracy_score(y_test, y_fitted)
    size = len(X_test)
    misclassified = np.sum(y_test != y_fitted)
    
    return accuracy_score, size, misclassified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages misclassified out of {total}")

if __name__ == "__main__":
    main()
