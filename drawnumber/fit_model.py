#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:19:20 2020

@author: ecem
"""

from drawnumber import model
from sklearn.model_selection import train_test_split
import keras
import pandas as pd
import numpy as np

np.random.seed(2)

img_rows, img_clmns = 28, 28
num_classes = 10

train = pd.read_csv("train.csv")

train_pixel = train.drop("label", axis=1)
train_pixel = train_pixel.astype('float32')
train_pixel /= 255.0
train_array = np.array(train_pixel)
train_label = train.loc[:, "label"]
train_label = keras.utils.to_categorical(train_label, num_classes)

train_array = train_array.reshape(train_pixel.shape[0], img_rows, img_clmns, 1)
input_shape = (img_rows, img_clmns, 1)

X_train, X_test, Y_train, Y_test = train_test_split(train_array, train_label, test_size=0.2)


model = model.create_model(input_shape)
model.fit(X_train, Y_train, epochs=50, batch_size=128)
loss, ac = model.evaluate(X_test, Y_test)
model.save("digit_model.h5")
