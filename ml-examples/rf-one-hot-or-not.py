#!/usr/bin/env python

"""
example that looks into the question as to whether we should 
one-hot encode or not before random forests.
"""

import os
import re
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, f1_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

## variables
rs = 42


## load data
df = pd.read_csv(os.path.join("..","data","titanic.csv"))
df.columns = [re.sub("\s+","_",c.lower()) for c in df.columns]
df.drop(columns=['name'],inplace=True)

numeric_features = ['age', 'siblings/spouses_aboard','parents/children_aboard', 'fare']
categorical_features = ['pclass','sex', 'age']

print(df.head())
print(df.columns)

## extract target
y = df.pop('survived')

## preprocessing pipeline
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())])

categorical_transformer1 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])
categorical_transformer2 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing'))])

preprocessor1 = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer1, categorical_features)])

preprocessor2 = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer2, categorical_features)])

## train-test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.25, stratify=y, random_state=rs)

param_grid_rf = {
    'rf__n_estimators': [20,50,100,150],
    'rf__max_depth': [4, 5, 6, 7, 8],
    'rf__criterion': ['gini', 'entropy']
}

pipe1 = Pipeline(steps=[('pre', preprocessor1),
                        ('rf',RandomForestClassifier())])
grid = GridSearchCV(pipe1, param_grid=param_grid_rf, cv=5, iid=False, n_jobs=-1)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)
print("\nWith OHE\n")
print("-->".join(pipe1.named_steps.keys()))
#best_params = dict(best_params, **grid.best_params_)
print("f1_score",round(f1_score(y_test, y_pred,average='binary'),3))


print("\nWithout OHE\n")
pipe2 = Pipeline(steps=[('pre', preprocessor2),
                        ('rf',RandomForestClassifier())])
grid = GridSearchCV(pipe2, param_grid=param_grid_rf, cv=5, iid=False, n_jobs=-1)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)
print("-->".join(pipe2.named_steps.keys()))
#best_params = dict(best_params, **grid.best_params_)
print("f1_score",round(f1_score(y_test, y_pred,average='binary'),3))
