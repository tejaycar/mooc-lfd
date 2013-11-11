# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 00:57:33 2013

@author: Tejay Cardon
visualize pla
"""

from LinearRegressionDecay import runLR
import numpy  as np    

train = np.genfromtxt("in.dta")
x1 = train[:,0]
x2 = train[:,1]
x = np.transpose(np.array([x1,x2,x1**2,x2**2,x1*x2,abs(x1-x2),abs(x1+x2)]))
x = np.insert(x, 0, np.ones((1,x1.size)), axis=1)

y = train[:,2]

test = np.genfromtxt("out.dta")
testx1 = test[:,0]
testx2 = test[:,1]
testy = test[:,2]
testx = np.transpose(np.array([testx1,testx2,testx1**2,testx2**2, testx1*testx2, abs(testx1 - testx2), abs(testx1 + testx2)]))
testx = np.insert(testx, 0, np.ones((1,testx1.size)), axis=1)

outBest = 100
best = 50
k = -10
while k < 10:
    i,o,w = runLR(x, y, show=False, X=testx, truthX=testy, lam=10**k)
    
    out = float(o)/testx1.size
    print float(i)/x1.size
    print out
    if out < outBest:
        outBest = out
        best = k
    k += 1
        
print best