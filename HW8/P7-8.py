# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:50:19 2013

@author: Tejay Cardon
"""

import numpy  as np   
from sklearn import svm
from sklearn.cross_validation import KFold

train = np.genfromtxt("features.train")

mask = np.logical_or(train[:,0] == 5, train[:,0] == 1)
train = train[mask]

error = np.empty([100,5,10])
print error.shape

def run(x, y, cvx, cvy, Cin):
   clf = svm.SVC(C=Cin, kernel='poly', degree=2, coef0=1.0, gamma=1.0)
   clf.fit(x,y)
   predict = clf.predict(cvx)
   #predictIn = clf.predict(x)
   Ecv = np.sum(np.where(cvy == predict, 0.0, 1.0))/cvy.size
   #Ein = np.sum(np.where(y == predictIn, 0.0, 1.0))/y.size
   #print "for C = " + str(Cin) + ", Ecv = " + str(Ecv) +  " Ein = " + str(Ein)
   return Ecv 
   
def runOnce(train, count):
    x = train[:,1:]
    y = np.where(train[:, 0] == 1, 1, -1)
    
    kf = KFold(len(x), n_folds=10, indices=False, shuffle=True)
    for c_index in range(0,5):
        fold = 0
        for trainMask, testMask in kf:
            error[count, c_index, fold] = run(x[trainMask], y[trainMask], x[testMask], y[testMask], .0001*(10**c_index))  
            fold += 1   
            
    return np.argmin(np.sum(error[count, :, :], 1))
     
choice = np.zeros((5))
for i in range(100):
    choice[runOnce(train, i)] += 1
    
print choice
print np.sum(np.sum(error, 0), 1)/10000.0
    
        
      

