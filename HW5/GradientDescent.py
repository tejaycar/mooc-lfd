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

def newu(u, v):
    return u - (lr * (2*(e**v + 2*v*e**-u)*(u*e**v - 2*v*e**-u)))
    
def newv(u, v):
    return v - (lr * (2*(u*e**v - 2*e**-u)*(u*e**v - 2*v*e**-u)))

iter = 1
err = error(u,v)
while iter < 500:
    print "on iter " + str(iter) + " error = " + str(err) + " u,v = " + str(u) + "," + str(v)
    if err < 10**-14:
        break    
    uTemp = newu(u,v)
    vTemp = newv(u,v)
    u = uTemp
    v = vTemp
    err = error(u,v)
    iter += 1
 