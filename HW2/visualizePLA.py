# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 00:57:33 2013

@author: Tejay Cardon
visualize pla
"""

from utils import points2weights
from pla import runPla
import numpy  as np
    
sum = 0.0
runs = 10
d = 10
for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)

    trainings, w = runPla(x,f,show=True)
    sum += trainings
print "Average of " + str(sum/runs) + " iterations"