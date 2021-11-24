#!/usr/bin/env python

"""
simple SVM example
"""


from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
    
## import some data to play with
iris = datasets.load_iris()

## Take only the first two features
X = iris.data[:, :2]
y = iris.target

## Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

## Specify parameters and model
kernel = 'rbf'
C = 1.0
gamma = 0.5
clf = svm.SVC(kernel='rbf', gamma=gamma, C=C)

## fit model
clf = clf.fit(X_train, y_train)

## evaluate the model fit
y_pred = clf.predict(X_test)
report = precision_recall_fscore_support(y_test, y_pred, average='macro')
print("------------------")
for m,v in zip(["precision","recall","fscore","support"],report):
    if isinstance(v,float):
        print(m,round(v,4))
    else:
        print(m,v)
print("------------------")
