# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-6
"""

import numpy as np
import LinearRegression as lr
from utils import points2weights

wrongOut = 0.0
runs = 1000
d = 100
D = 1000
for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)    
    truth = np.sign(np.dot(x,f))
    X = np.insert(np.random.random((D,2)) * 2 - 1,0,np.ones((1,D)),axis=1)
    truthX = np.sign(np.dot(X,f))    
    
    i,o,w = lr.runLR(x, truth, X=X, truthX=truthX)
    wrongOut += o
print "Average of " + str(wrongOut/runs) + " wrong out of sample per run"
print "%f incorrect on average out of sample"%((wrongOut/runs/D))
fractionWrong = (wrongOut/runs)/D
print "%f incorrect on average out of sample"%(fractionWrong)

a = abs(fractionWrong - 0)
b = abs(fractionWrong - 0.001)
c = abs(fractionWrong - 0.01)
d = abs(fractionWrong - 0.1)

if min([a,b,c,d]) == a :
    print "Answer is A"
elif min([a,b,c,d]) == b :
    print "Answer is B"
elif min([a,b,c,d]) == c :
    print "Answer is C"
elif min([a,b,c,d]) == d :
    print "Answer is D"
else: 
    print "Tie, or you blew it, one of the two"
    