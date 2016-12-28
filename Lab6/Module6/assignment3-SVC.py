# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 


#Load up the /Module6/Datasets/parkinsons.data data set into a variable X, 
#being sure to drop the name column.
#
X = pd.read_csv('Datasets/parkinsons.data')
X.drop(labels=['name'], axis=1, inplace=True)
#print(X.head())

#Splice out the status column into a variable and delete it from X.
#
y = X.status
#print(y.head())
X.drop(labels=['status'], axis=1, inplace=True)

#Perform a train/test split. 30% test group size, with a random_state equal to 7.
#
#Normalizer(), MaxAbsScaler(), MinMaxScaler(), and StandardScaler().

from sklearn import preprocessing
T = preprocessing.StandardScaler().fit(X)         

tra = T.transform(X)


"""
from sklearn.decomposition import PCA
pca = PCA(n_components = 14)
tra = pca.fit_transform(tra)
"""

from sklearn import manifold
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

best_score = 0

for k in range(2, 6):
    for l in range(4, 7):
        iso = manifold.Isomap(n_neighbors = k, n_components = l)
        S = iso.fit_transform(tra)
        
        X_train, X_test, y_train, y_test = train_test_split(S, y, test_size=0.30, random_state=7)

        for i in np.arange(start = 0.05, stop = 2.00, step = 0.05):
            for j in np.arange(start = 0.001, stop = 0.100, step = 0.001):
                model = SVC(C = i, gamma = j)
                model.fit(X_train, y_train)
                score = model.score(X_test, y_test)
                if score > best_score:
                    best_score = score

print ("The highest score obtained:", best_score)
print ("C value:", model.C) 
print ("gamma value:", model.gamma)
print ("isomap n_neighbors:", iso.n_neighbors)
print ("isomap n_components:", iso.n_components)
"""        
from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=7)
X_train, X_test, y_train, y_test = train_test_split(tra, y, test_size=0.30, random_state=7)

#Create a SVC classifier. Don't specify any parameters, just leave everything as default. 
#Fit it against your training data and then score your testing data.
#
from sklearn.svm import SVC
"
model = SVC()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(score)
"
#What accuracy did you score?
#
#0.813559322034

#Program a naive, best-parameter searcher by creating a nested for-loops. 
#The outer for-loop should iterate a variable C from 0.05 to 2, using unit 0.05 increments. 
#The inner for-loop should increment a variable gamma from 0.001 to 0.1, using 0.001 unit increments. 
#As you know, Python ranges won't allow for float intervals, so you'll have
#to do some research on NumPy ARanges, if you don't already know how to use them.
#Since the goal is to find the parameters that result in the model having the best score, you'll need a
#best_score = 0 variable that you initialize outside of the for-loops. 
#Inside the for-loop, create a model and pass in the C and gamma parameters into the class constructor.

best_score = 0

for i in np.arange(start = 0.05, stop = 2.00, step = 0.05):
    for j in np.arange(start = 0.001, stop = 0.100, step = 0.001):
        model = SVC(C = i, gamma = j)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        if score > best_score:
            best_score = score

print ("The highest score obtained:", best_score)
print ("C value:", model.C) 
print ("gamma value:", model.gamma)           
"""            

#Right after you splice out the status column, but before you process the train/test split, 
#inject SciKit-Learn pre-processing code. Unless you have a good idea which one is going to work best, 
#you're going to have to try the various pre-processors one at a time, 
#checking to see if they improve your predictive accuracy. - Line 28 and 29.
#Normalizer(), MaxAbsScaler(), MinMaxScaler(), and StandardScaler().
#After trying all of these scalers, what is the new highest accuracy score you're able to achieve?
#0.932203389831
            