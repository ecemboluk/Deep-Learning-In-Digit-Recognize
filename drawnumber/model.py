#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:40:25 2020

@author: ecem
"""
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D


def create_model(input_shape):
    
    model = Sequential()
    model.add(Conv2D(6, kernel_size=(5, 5), activation="relu", input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(16, kernel_size=(5, 5), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model
    

