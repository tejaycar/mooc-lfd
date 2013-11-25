# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:50:19 2013

@author: Tejay Cardon
"""

import numpy  as np   
from sklearn import svm

train = np.genfromtxt("features.train")

Cin = 0.01
Q = 2

x = train[:,1:]

def run(claz):
   y = np.where(train[:, 0] == claz, 1, -1)
     
   clf = svm.SVC(C=Cin, kernel='poly', degree=Q, coef0=1.0, gamma=1.0)
   clf.fit(x,y)
   predict = clf.predict(x)
   print "for " + str(claz) +" vs all, Ein = " + str(np.sum(np.where(y == predict, 0.0, 1.0))/y.size)
   print clf.n_support_

for claz in range(0,10):
    run(claz)