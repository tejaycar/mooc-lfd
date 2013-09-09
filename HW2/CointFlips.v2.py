# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 15:58:58 2013

@author: Tejay Cardon

*This is my thirt python program of all time

Re-write of HW2 prb. 1 to do it all in one large 3-d array
"""

import numpy as np
from random import randint

def flipAverages(coins, flips, runs):
    allFlips = np.random.randint(0,2,(runs,coins,flips))
    print "Average first = " + str(np.sum(allFlips[:,0,:])/(runs*flips))
    print "Average min = " + str(np.sum(np.min(np.sum(allFlips, axis=2),axis=1))/(flips*runs))
    randomCoin = randint(0,coins -1)
    print "Average random = %f"%(np.sum(allFlips[:,randomCoin,:])/(runs*flips))

    
flipAverages(1000.0,10.0,100000.0)
#flipAverages(10.0,10.0,20.0)
    
    