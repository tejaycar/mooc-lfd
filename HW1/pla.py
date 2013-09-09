# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 22:40:31 2013

@author: Tejay cardon
HW1 problems 7-10
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from random import randint

def runF(line, testPoints):
    result = ((line[1][0] - line[0][0]) * (testPoints[:,2] - line[0][1]) - (line[1][1] - line[0][1]) * (testPoints[:,1] - line[0][0]))
    result = sp.sign(result)
    return result
    
def plot(right, wrong, axis, w):
    if not show:
        return
    plt.subplot(axis)
    plt.cla()
    plt.plot([-w[0][0]/w[0][1],0], [0, -w[0][0]/w[0][2]], 'b--')
    plt.plot(right[:,0], right[:,1], 'g+')
    plt.plot(wrong[:,0],wrong[:,1],'rx')
    plt.ylim([-1,1])
    plt.xlim([-1,1])
    plt.draw()

def oneIter(w, g, f):
    i = randint(0,f.size - 1)
    w += f[i] * g[i]
    
    
def runOnce(d, show):
    f = np.random.random((2,2)) * 2 - 1
    
    #print "f = " + str(f)
    
    x = np.random.random((d,2)) * 2 - 1
    x = np.insert(x,0,np.ones((1,d)), axis=1)
    w = np.zeros((1,3))
    
    #print "x = " + str(x)
    truth = runF(f, x)
    #print "truth = " + str(truth)
    
    green = np.empty([0,2])
    red = np.empty([0,2])
    for i in range (0,truth.size):
        if truth[i] > 0:
            green = np.append(green, [x[i,1:]], axis=0)
        else:
            red = np.append(red, [x[i,1:]], axis=0)
    
    plt.clf
    plt.subplot(311)
    plt.cla
    plt.plot(f[:,0],f[:,1], 'r-')
    plt.plot(green[:,0], green[:,1], 'go')
    plt.plot(red[:,0],red[:,1],'ro')
    
    right = np.empty([0,2])
    wrong = np.empty([0,2])
    count = 0
    while right[:].size < x[:].size:
        right = np.empty([0,2])
        wrong = np.empty([0,3])
        green = np.empty([0,2])
        red = np.empty([0,2])
        shouldHaveBeen = np.empty([0,1])
        count += 1
        g = sp.sign(np.dot(x, np.transpose(w)))
        #print "g = " + str(g)
        for i in range (0,truth.size):
            if g[i] > 0:
                green = np.append(green, [x[i,1:]], axis=0)
            else:
                red = np.append(red, [x[i,1:]], axis=0)
            
            if g[i] == truth[i]:
                right = np.append(right, [x[i,1:]], axis=0)
            else:
                wrong = np.append(wrong, [x[i]], axis=0)
                shouldHaveBeen = np.append(shouldHaveBeen, truth[i])
        
        plot(green,red,312, w)
        plot(right, wrong[:,1:], 313, w)
        if wrong.size == 0:
            break
        oneIter(w, wrong, shouldHaveBeen)
        if show:
            plt.pause(.5)
        print count
    return count
    
sum = 0
runs = 1
for i in range(0,runs):
    print "Running test # " + str(i)
    sum += runOnce(100, True)
print "Average of " + str(sum/runs) + " iterations"
    