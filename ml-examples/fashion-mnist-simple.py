#!/usr/bin/env python
"""
analyze a subset of the fashion mnist data
using dimension reduction and classic machine learning
"""


import sys
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
from sklearn.decomposition import PCA


## use keras to load fashion mnist
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() 
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']



## look at sample image
#plt.figure()
#plt.imshow(train_images[0])
#plt.colorbar()
#plt.grid(False)
#plt.show()

## display the first 25 images from the training set and 
# display the class name below each image
# verify that data is in correct format

#plt.figure(figsize=(10,10))
#for i in range(25):
#	plt.subplot(5,5, i+1)
#	plt.xticks([])
#	plt.yticks([])
#	plt.grid(False)
#	plt.imshow(train_images[i], cmap=plt.cm.binary)
#	plt.xlabel(class_names[train_labels[i]])
#plt.show()


print(train_images.shape)
print(test_images.shape)

## scale the values to a range of 0 to 1 of both data sets
train_images = train_images / 255.0
test_images = test_images / 255.0

## subset the data to only the first 5 classes
print("... subsetting data")
train_subset = np.in1d(train_labels, np.array([0,1,2,3,4]))
test_subset = np.in1d(test_labels, np.array([0,1,2,3,4]))

train_labels = train_labels[train_subset]
test_labels = test_labels[test_subset]
train_images = train_images[train_subset]
test_images = test_images[test_subset]

print(test_images.shape)

print(test_images.flatten().shape)
sys.exit()


X_train = [i.flatten() for i in train_images]
X_test = [i.flatten() for i in test_images]



print(train_images.shape)
print(test_images.shape)


pca = PCA(n_components=4)
X_r = pca.fit(X_train)



print("---------------------")
print("X_train", X_train.shape)
class_info = list(sorted(Counter(y_train).items()))
print("num classes", len(class_info), [i[0] for i in class_info])
print("class samples", [i[1] for i in class_info])
print("class balance", [round(i[1]/X.shape[0],2) for i in class_info])
print("---------------------")



print('good')
