# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 21:24:37 2013

@author: family
"""

from utils import points2weights, plot
import numpy  as np
import random
from matplotlib.pyplot import pause
from scipy import e

runs = 100

N = 100
lr = .01

def mag(old, new):
    return np.sqrt((old[0] - new[0])**2 + (old[1] - new[1])**2 + (old[2] - new[2])**2)
    
def getError(x,y,w):
    temp = np.dot(x,w)
    temp = np.dot(y,temp)
    temp = e**(-temp)
    temp = np.log(1 + temp)
    return temp
    
def gradient(x,y,w):
    top = y*x
    bottom = 1 + e**(y * np.dot(x,w))
    return top/bottom
    
sum = 0.0
run = 0.0
while run < runs:
    f = points2weights(np.random.random((2,2)) * 2 - 1)
    x = np.insert(np.random.random((N,2)) * 2 - 1,0,np.ones((1,N)), axis=1)
    testSet = np.insert(np.random.random((N*10,2)) * 2 - 1,0,np.ones((1,N*10)), axis=1)
    
    y = np.sign(np.dot(x,f))
    testTruth = np.sign(np.dot(testSet,f))
    
    w = np.zeros(3)
    
    green = x[(y == 1), 1:]
    red = x[(y != 1), 1:]
    plot(green, red, f, axis=311, show=True)
    count = 0
    
    while count < 1000:
        oldW = np.copy(w)
        element = 0
        while element < N:
            w += lr * gradient(x[element],y[element],w)
            element += 1
        prediction = np.sign(np.dot(x,np.transpose(w)))
        right = x[(prediction == y),1:]
        wrong = x[(prediction != y),1:]
        plot(right, wrong, w, show=False, axis=313)#, xlim=[-5,5], ylim=[-5,5])
        #pause(.05)
        if mag(oldW, w) < 0.01:
            break
        count += 1
    
    prediction = np.sign(np.dot(testSet,np.transpose(w)))
    right = testSet[(prediction == testTruth),1:]
    wrong = testSet[(prediction != testTruth),1:]
    plot(right, wrong, w, show=True, axis=313)
    pause(.2)
    run += 1
    sum += count

print sum/runs