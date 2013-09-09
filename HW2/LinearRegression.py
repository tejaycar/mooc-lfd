# -*- coding: utf-8 -*-
"""
Created on Thu Sep 05 22:40:31 2013

@author: Tejay cardon
HW1 problems 7-10
"""

import numpy as np
from utils import plot

def train(x, truth):
    pseudoIn= np.linalg.pinv(x)
    return np.dot(pseudoIn, truth)
    
def runLR(x, truth, show=False, X=None, truthX=None):
    
    w = train(x,truth)
    #print "w = " + str(w)    

    prediction = np.sign(np.dot(x,w))
    
    green = x[(prediction == 1), 1:]
    red = x[(prediction < 1), 1:]  
    plot(green, red, w, show=show, axis=312 if X == None else 323)
    
    right = x[(prediction == truth),1:]
    wrong = x[(prediction != truth),1:]
    plot(right, wrong, w, show=show, axis=313 if X == None else 325)
    wrongIn = wrong[:,0].size    
    
    if X != None:
        predictionOut = np.sign(np.dot(X,w))
        
        green = X[(predictionOut == 1), 1:]
        red = X[(predictionOut < 1), 1:]  
        plot(green, red, w, show=show, axis=324)
        
        right = X[(predictionOut == truthX),1:]
        wrong = X[(predictionOut != truthX),1:]
        plot(right, wrong, w, show=show, axis=326)
    
    return wrongIn, wrong[:,0].size, w
    

