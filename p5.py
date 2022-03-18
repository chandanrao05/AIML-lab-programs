# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:02:37 2022

@author: chand
"""
import numpy as np
from backpropagation.NeuralNetwork import NeuralNetwork
from backpropagation.Backpropagation import Backpropagation
from backpropagation.Sigmoid import Sigmoid

x = np.array(([2,9],[1,5],[3,6]), dtype=float)
y = np.array(([92],[86],[89]), dtype=float)

x = x/np.amax(x,axis=0)
y = y/100

nn = NeuralNetwork(2,3,1)
nn.initalize_weights(True)

activation_function = Sigmoid()

bp = Backpropagation(nn,5000,.1,activation_function)
bp.train(x,y)
bp.predict(x,y)