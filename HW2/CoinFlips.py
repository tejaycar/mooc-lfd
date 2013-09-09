# -*- coding: utf-8 -*-
"""
Created on Sun Sep 08 15:58:58 2013

@author: Tejay Cardon

*This is my second python program of all time

HW2 prb. 1
"""

import numpy as np
from random import randint

def runOnce(debug, numCoins, flipsPerCoin):
    flips = np.random.randint(0,2,(numCoins,flipsPerCoin))
    if debug >= 3:        
        print "all flips = " + str(flips)
    if debug >= 2:
        print "heads = " + str(np.sum(flips,axis=1))
    randomCoin = randint(0,numCoins - 1)
    first = np.sum(flips[0])
    randomHeads = np.sum(flips[randomCoin])
    minHeads = np.min(np.sum(flips, axis=1))
    if debug >= 1:    
        print "First coin heads = " + str(first)
        print "Random coin #" + str(randomCoin) + " heads = " + str(randomHeads)
        print "Min coin = " + str(minHeads)
    
    if first < minHeads or randomHeads < minHeads:
        print flips
    return first, randomHeads, minHeads
        
#print runOnce(1,5,5)

debug = 0
first = 0.0
rand = 0.0
minimum = 0.0
runs = 100000
c=0
zero = 0.0
one = 0.0
two = 0.0
more = 0.0
for run in range(0,runs):
    c += 1
    print "runing  iteration # " + str(run)
    f, r, m = runOnce(debug,1000,10)
    if debug > 3:
        print "f = " + str(f)
        print "m = " + str(m)
        print "r = " + str(r)
        print "minimum = " + str(minimum)
    first += f
    rand += r
    minimum += m
    if m == 0:
        zero += 1
    elif m == 1:
        one += 1
    elif m ==  2:
        two  += 1
    else:
        more += 1

print "ran %s times"%(c)

print "Average first = " + str(first/runs)
print "Average random = " + str(rand/runs)
print "Average min = " + str(minimum/runs)

print "zero =  %d"%(zero)
print "one =  %d"%(one)
print "two =  %d"%(two)
print "more =  %d"%(more)