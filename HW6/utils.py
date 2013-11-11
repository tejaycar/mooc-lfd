# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 00:13:55 2013

@author: Tejay Cardon
HW 2 support
"""

import numpy as np
import matplotlib.pyplot as plt

def points2weights(points):
    slope = (points[1][1] - points[0][1])/(points[1][0] - points[0][0])
    w = np.array([(-points[0][1]+(points[0][0]*slope)),-slope,1.0])
    w = w/w[0]
    return w
    
def plot(right, wrong, line, show=False, axis=111, other=None, xlim=None, ylim=None):
    if not show:
        return
    plt.subplot(axis)
    plt.cla()
    plt.plot([1, -1], [(-line[0] - line[1])/line[2], (-line[0] + line[1])/line[2]], 'b--')
    plt.plot(right[:,0], right[:,1], 'g+')
    plt.plot(wrong[:,0],wrong[:,1],'rx')
    plt.ylim(ylim or [-1,1])
    plt.xlim(xlim or [-1,1])
    if other != None:
        plt.plot(other[0], other[1], other[2])
    plt.draw()