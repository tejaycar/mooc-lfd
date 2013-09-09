# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 00:57:33 2013

@author: Tejay Cardon
visualize pla
"""

from utils import points2weights, plot
from LinearRegression import runLR
import numpy  as np
from matplotlib.pyplot import pause
    
runs = 10
d = 1000

for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    truth = np.sign(np.dot(x,f))
    i,o,w = runLR(x, truth, show=True)
    
    green = x[(truth == 1), 1:]
    red = x[(truth != 1), 1:]
    plot(green, red, f, axis=311, show=True)
    pause(.5)