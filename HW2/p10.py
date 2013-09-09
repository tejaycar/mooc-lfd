# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-10
"""

import numpy as np
import LinearRegression as lr

wrongIn = 0.0
runs = 1000
d = 100
aveW = np.zeros((6))

for i in range(0,runs):
    print "Running test # " + str(i)
    
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    x = np.append(x, x[:,1:2] * x[:,2:3], axis=1)
    x = np.append(x, np.square(x[:,1:3]), axis=1)
    truth = np.sign(np.square(x[:,1]) + np.square(x[:,2]) - .6)
    noise = np.append(np.ones((d*.9)), np.ones((d - d*.9)) * -1, axis=0)
    np.random.shuffle(noise)
    truth *= noise
    i,o,w = lr.runLR(x, truth, show=False)
    
    wrongIn += i
    aveW = aveW + w

wrongIn = 0.0    
for i in range(0,runs):
    print "Running test # " + str(i)
    
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    x = np.append(x, x[:,1:2] * x[:,2:3], axis=1)
    x = np.append(x, np.square(x[:,1:3]), axis=1)
    truth = np.sign(np.square(x[:,1]) + np.square(x[:,2]) - .6)
    noise = np.append(np.ones((d*.9)), np.ones((d - d*.9)) * -1, axis=0)
    np.random.shuffle(noise)
    truth *= noise
    prediction = np.sign(np.dot(x,(aveW/runs)))
    
    wrongIn += (x[(prediction != truth),1:])[:,0].size

print "Average of " + str(wrongIn/runs) + " wrong in sample per run"
fractionWrong = (wrongIn/runs)/d
print "%f incorrect on average in sample"%(fractionWrong)
print "ave w is " + str(aveW/runs)

a = abs(fractionWrong - 0)
b = abs(fractionWrong - 0.1)
c = abs(fractionWrong - 0.3)
d = abs(fractionWrong - 0.5)
e = abs(fractionWrong - 0.8)

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