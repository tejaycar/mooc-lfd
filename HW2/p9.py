# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 23:59:47 2013

@author: Tejay Cardon
HW2-9
"""

import numpy as np
import LinearRegression as lr
import matplotlib.pyplot as plt

wrongIn = 0.0
runs = 1000
d = 100
aveW = np.zeros((1,6))

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
    
#    plotX = np.linspace(-1,1,1000)
#    plotY = np.sqrt(np.square(plotX) * -1 + .6) 
#    plt.subplot(311)
#    plt.cla()
#    plt.plot(plotX,plotY,'b-')
#    plt.plot(plotX,-plotY,'b-')
#    green = x[(truth == 1), 1:]
#    red = x[(truth < 1), 1:]  
#    plt.plot(green[:,0], green[:,1], 'go')
#    plt.plot(red[:,0], red[:,1], 'ro')
    
    wrongIn += i
    aveW = aveW + w
print "Average of " + str(wrongIn/runs) + " wrong in sample per run"
fractionWrong = (wrongIn/runs)/d
print "%f incorrect on average in sample"%(fractionWrong)
print "ave w is " + str(aveW/runs)