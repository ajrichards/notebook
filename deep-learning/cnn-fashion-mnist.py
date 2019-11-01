#!/usr/bin/env python

## if you wish to work with tensorflow v1 then ask it to emulate version 2 behavior
#import tensorflow.compat.v2 as tf
#tf.enable_v2_behavior()
#print(tf.__version__)

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import csv
import joblib
import time
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

## check hardware availability
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


def get_data():
    ### load the data  
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() 
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 
                   'Sneaker', 'Bag', 'Ankle boot']

    ## Normalize pixel values to be between 0 and 1
    #train_images, test_images = train_images / 255.0, test_images / 255.0
        
    X_train = train_images
    X_test = test_images
    y_train = train_labels
    y_test = test_labels

    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255
    
    return(X_train,y_train,X_test,y_test)


def summarize_data(X_train,y_train,X_test,y_test):
    print("-------------------------------------------")
    print("X_train: {}".format(X_train.shape))
    class_info = list(sorted(Counter(y_train).items()))
    print("num classes: {}, classes: {}".format(len(class_info), [i[0] for i in class_info]))
    print("class samples: {}".format([i[1] for i in class_info]))
    print("class balance: {}".format([round(i[1]/X_train.shape[0],2) for i in class_info]))
    print(X_train.shape)
    print("-------------------------------------------")


def build_mlp(activation_fn='relu'):
    """
    create a simple cnn
    """
    
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))
    model.add(keras.layers.Dense(128, activation=activation_fn))
    model.add(keras.layers.Dense(10, activation='softmax'))    

    return(model)


def build_cnn(activation_fn='relu',dropout=None):
    """
    create a simple cnn
    """

    num_classes = np.unique(y_train).size
    
    if not dropout:
        dropout = [False,False]
    
    model = keras.Sequential()
    
    model.add(keras.layers.Conv2D(28, (3, 3), activation=activation_fn, input_shape=(28, 28, 1)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    
    if dropout[0]:
        model.add(tf.keras.layers.Dropout(0.3))
    
    model.add(keras.layers.Conv2D(64, (3, 3), activation=activation_fn))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    
    if dropout[0]:
        model.add(tf.keras.layers.Dropout(0.3))
    
    model.add(keras.layers.Conv2D(64, (3, 3), activation=activation_fn))
    
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation=activation_fn))
    model.add(keras.layers.Dense(num_classes, activation='softmax'))
    

    return(model)


def train_network(model_name,model,loss_fn,optimizer='adam'):
    """
    compile, train and save the cnn
    """

    ## save model and logfile
    save_dir = 'saved'
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

    saved_model = os.path.join(save_dir,"{}.h5".format(model_name))

    ## compile the model
    if not os.path.exists(saved_model):
        ## compile and fit model
        model.compile(optimizer=optimizer,
                      loss=loss_fn,
                      metrics=['accuracy'])

        model.fit(X_train,
                  y_train,
                  batch_size=64,
                  epochs=10,
                  validation_data=(X_test, y_test))
        model.save(saved_model)

        ## evaluate model
        test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2)    
        
        ## save a log file
        log_file = os.path.join(save_dir,"{}.log".format(model_name)) 
        with open(log_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["loss_function",loss_fn])
            writer.writerow(["optimizer", optimizer])
            writer.writerow(["test_loss",test_loss])
            writer.writerow(["test_acc",test_acc])

    else:
        print("... loading saved model")
        model = keras.models.load_model(saved_model)
        
            
    return(model)
        
if __name__ == "__main__":


    ## get data
    X_train,y_train,X_test,y_test = get_data()
    summarize_data(X_train,y_train,X_test,y_test)

    ## build and train a MLP
    ## YOUR CODE HERE (build and train a MLP)
    model_mlp = build_mlp(activation_fn='relu')
    model_mlp = train_network("simple_mlp", model_mlp, "sparse_categorical_crossentropy",
                              X_train,
                              y_train,
                              X_test,
                              y_test,
                              optimizer='adam')

    ## add the channel dimensions to your data
    X_train_1 = np.expand_dims(X_train, -1)
    X_test_1 = np.expand_dims(X_test, -1)

    model_cnn = build_cnn(activation_fn='relu')
    train_network("cnn", model_cnn, "categorical_crossentropy", 
                  X_train_1,
                  y_train,
                  X_test_1,
                  y_test, 
                  optimizer='adam')

    
    ## make predictions
    #predictions = model.predict(test_images)
    #predictions = np.argmax(predictions)
