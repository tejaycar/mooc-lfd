# -*- coding: utf-8 -*-
"""
Created on Wed Oct 02 07:06:07 2013

@author: family
"""

from utils import points2weights
from pla_revisited import runPla
import numpy  as np
    
sum = 0.0
runs = 1000
d = 10
for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)

    trainings, w = runPla(x,f,show=False)
    sum += trainings
print "Average of " + str(sum/runs) + " iterations"