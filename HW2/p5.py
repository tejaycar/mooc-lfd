# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-5
"""

import numpy as np
import LinearRegression as lr
from utils import points2weights

wrongIn = 0.0
runs = 1000
d = 100

for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    truth = np.sign(np.dot(x,f))
    i,o,w = lr.runLR(x, truth)
    
    wrongIn += i
print "Average of " + str(wrongIn/runs) + " wrong in sample per run"
fractionWrong = (wrongIn/runs)/d
print "%f incorrect on average in sample"%(fractionWrong)

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
    


