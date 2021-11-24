#!/usr/bin/env python
"""
analyze a subset of the fashion mnist data
using dimension reduction and classic machine learning
"""

from joblib import dump, load
import sys
import os
import time
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.manifold import TSNE

make_plots = False

## use keras to load fashion mnist
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() 
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

## look at sample image
if make_plots:
    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()

## display the first 25 images from the training set and 
# display the class name below each image
# verify that data is in correct format

if make_plots:
    plt.figure(figsize=(10,10))
    
    for i in range(25):
        
        plt.subplot(5,5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i+50], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i+50]]) 
    plt.show()

print(train_images.shape)
print(test_images.shape)

## scale the values to a range of 0 to 1 of both data sets
train_images = train_images / 255.0
test_images = test_images / 255.0

## subset the data to only the first 3 classes
print("... subsetting data")

subset = np.array([0,1,2,3,4])
train_subset = np.in1d(train_labels,subset)
train_labels = train_labels[train_subset]
train_images = train_images[train_subset]

test_subset = np.in1d(test_labels,subset)
test_labels = test_labels[test_subset]
test_images = test_images[test_subset]

## flatten the images to be 784 pixel vectors
X_train = np.array([i.flatten() for i in train_images])
X_test = np.array([i.flatten() for i in test_images])
y_train = train_labels
y_test = test_labels

## specifiy pipeline
pipe = Pipeline([('tsne', TSNE(init='pca')),
                  ('svm', SVC(class_weight='balanced'))])

param_grid = {
    'tsne__n_components': [5,10,25],
    'svm__C': [0.001,0.1,1.0,10.0],
    'svm__gamma': [0.1,0.01]
}

print("---------------------")
print("X_train", X_train.shape)
class_info = list(sorted(Counter(y_train).items()))
print("num classes", len(class_info), [i[0] for i in class_info])
print("class samples", [i[1] for i in class_info])
print("class balance", [round(i[1]/X_train.shape[0],2) for i in class_info])
print("---------------------")


saved_model = 'tsne-svm.joblib'
if not os.path.exists(saved_model):
    time_start = time.time()
    grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, iid=False, n_jobs=-1)
    grid.fit(X_train, y_train)
    dump(grid, saved_model)
    print("train time", time.strftime('%H:%M:%S', time.gmtime(time.time()-time_start)))
else:
    print("loading {} from file".format(saved_model))
    grid = load(saved_model) 

## print best params
print(grid.best_params_)

## evaluate
y_pred = grid.predict(X_test)
print("-->".join(pipe.named_steps.keys()),"\n")
print(classification_report(y_test, y_pred),target_names=np.array(class_names)[subset])
print('good')
