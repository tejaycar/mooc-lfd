# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-7
"""


import numpy as np
from LinearRegression import runLR
from pla import runPla
from utils import points2weights

count = 0.0
runs = 1000
d = 10
for i in range(0,runs):
    print "Running test # " + str(i)
    
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    truth = np.sign(np.dot(x,f))
    i,o,w = runLR(x, truth)
    
    c, w = runPla(x,f,w=w)
    count += c

average = count/runs
print "average is %f"%(average)

a = abs(average - 1)
b = abs(average - 15)
c = abs(average - 300)
d = abs(average - 5000)
e = abs(average - 10000)

if min([a,b,c,d,e]) == a :
    print "Answer is A"
elif min([a,b,c,d,e]) == b :
    print "Answer is B"
elif min([a,b,c,d,e]) == c :
    print "Answer is C"
elif min([a,b,c,d,e]) == d :
    print "Answer is D"
elif min([a,b,c,d,e]) == e :
    print "Answer is E"
else: 
    print "Tie, or you blew it, one of the two"
    
    