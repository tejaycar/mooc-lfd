# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-8
"""

import numpy as np
import LinearRegression as lr
from utils import plot
from matplotlib.pyplot import pause

wrongIn = 0.0
runs = 1000
d = 1000
show=False

for i in range(0,runs):
    print "Running test # " + str(i)
    
    x = np.insert(np.random.random((d,2)) * 2 - 1,0,np.ones((1,d)), axis=1)
    truth = np.sign(np.square(x[:,1]) + np.square(x[:,2]) - .6)
    noise = np.append(np.ones((d*.9)), np.ones((d - d*.9)) * -1, axis=0)
    np.random.shuffle(noise)
    truth *= noise
    i,o,w = lr.runLR(x, truth, show=show)
    
    plotX = np.linspace(-1,1,1000)
    plotY = np.sqrt(np.square(plotX) * -1 + .6) 
    plotX = np.append(plotX, plotX, axis=1)
    plotY = np.append(plotY, -plotY, axis=1)
    green = x[(truth == 1), 1:]
    red = x[(truth < 1), 1:]  
    plot(green, red, [7,1,7], axis=311, show=show, other=[plotX, plotY,'b-'])
    pause(.1)
    
    wrongIn += i
print "Average of " + str(wrongIn/runs) + " wrong in sample per run"
fractionWrong = (wrongIn/runs)/d
print "%f incorrect on average in sample"%(fractionWrong)

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