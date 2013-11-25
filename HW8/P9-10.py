# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:50:19 2013

@author: Tejay Cardon
"""

import numpy  as np   
from sklearn import svm

train = np.genfromtxt("features.train")
test = np.genfromtxt("features.test")

mask = np.logical_or(train[:,0] == 5, train[:,0] == 1)
train = train[mask]
x = train[:,1:]
y = np.where(train[:, 0] == 1, 1, -1)

mask = np.logical_or(test[:,0] == 5, test[:,0] == 1)
test = test[mask]
xtest = test[:,1:]
ytest = np.where(test[:, 0] == 1, 1, -1)

def run(claz, Cin):
   clf = svm.SVC(C=Cin, kernel='rbf', gamma=1.0)
   clf.fit(x,y)
   predict = clf.predict(xtest)
   predictIn = clf.predict(x)
   print "for C = " + str(Cin) + ", Eout = " + str(np.sum(np.where(ytest == predict, 0.0, 1.0))/ytest.size) +  " Ein = " + str(np.sum(np.where(y == predictIn, 0.0, 1.0))/y.size)
   print clf.n_support_

Cin = .01
while Cin <= 10**6:
    run(1, Cin)
    Cin *= 100