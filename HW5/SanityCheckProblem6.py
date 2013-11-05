# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:10:30 2013

@author: family
"""

from scipy import e

u = 1.0
v = 1.0
lr = 0.1

def error(uin, vin):
    return (uin * e**vin - 2*vin*e**-uin)**2

print error(1.0, 1.0)
print error(0.713, 0.045)
print error(0.016, 0.112)
print error(-0.083, 0.029)
print error(0.045, 0.024)
  