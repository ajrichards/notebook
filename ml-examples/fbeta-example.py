#!/usr/bin/env python

"""
simple SVM example
"""

from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, fbeta_score, make_scorer
    
rs=42
X, y = make_classification(n_samples=3000, n_features=50, n_informative=20,
                           n_redundant=2, n_classes=2,
                           n_clusters_per_class=3,
                           weights=[0.5, 0.5],
                           class_sep=0.9, random_state=rs)

## Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=rs, stratify=y)

## Specify parameters and model
model = SVC(kernel='rbf')

ftwo_score = make_scorer(fbeta_score, beta=2, average='weighted')
param_grid = {
    'C': [0.1,0.5,1.0,10.0],
    'gamma': [0.01,0.1]
}

grid = GridSearchCV(model, param_grid=param_grid,
                    scoring=ftwo_score, cv=5)
## fit model
grid.fit(X_train, y_train)

## evaluate the model fit
y_pred = grid.predict(X_test)
print("F1_score", round(f1_score(y_test,y_pred,labels=y_pred),3))
print("Fbeta_score", round(fbeta_score(y_test,y_pred,labels=y_pred,beta=2.0),3))



