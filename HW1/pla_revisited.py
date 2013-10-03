# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 22:40:31 2013

@author: Tejay cardon
HW1 problems 7-10
"""


import numpy as np
from matplotlib.pyplot import pause
from utils import plot
from random import randint

def train(w, x, prediction, truth):
    bad = x[(prediction != truth)]
    shouldHaveBeen = truth[(prediction != truth)]
    i = randint(0,bad[:,0].size - 1)
    w += shouldHaveBeen[i] * bad[i]
    return w
    
def runPla(x, f, w=np.zeros((3)), show=False, X=None):
    
    truth = np.sign(np.dot(x,f))
    green = x[(truth == 1), 1:]
    red = x[(truth < 1), 1:]
        
    plot(green, red, f, show=show, axis=311)
    
    right = np.empty([0,2])
    wrong = np.empty([0,2])
    count = 0
    while right[:].size < x[:].size:
        prediction = np.sign(np.dot(x,w))
        #print "prediction = " + str(prediction)
    
        green = x[(prediction == 1), 1:]
        red = x[(prediction < 1), 1:]  
        plot(green, red, w, show=show, axis=312)
        
        right = x[(prediction == truth),1:]
        wrong = x[(prediction != truth),1:]
        plot(right, wrong, w, show=show, axis=313)
        if wrong.size == 0:
            break
        w = train(w, x, prediction, truth)
        count += 1
        if show:
            pause(.1)
    return count, w

    