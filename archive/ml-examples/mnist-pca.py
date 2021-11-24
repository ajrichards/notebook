#!/usr/bin/env python

from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
digits = load_digits()

X,y = digits.data, digits.target 


pca_digits=PCA(0.95) 
X_proj = pca_digits.fit_transform(X) 
print(X.shape, X_proj.shape)

