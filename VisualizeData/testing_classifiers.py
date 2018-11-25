import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import sys
from time import time


import matplotlib.pyplot as plt

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, ComplementNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.extmath import density
from sklearn import metrics


features = pd.read_csv('/home/amygdala/generated_datav2.csv',usecols=range(1, 11))
grades = pd.read_csv('/home/amygdala/generated_datav2.csv',usecols=range(11, 12))




features.ix[:,4] = list(features.ix[:,4].str.replace(" ","_"))
features.ix[:,8] = list(features.ix[:,8].str.replace(" ","_"))
features.ix[:,4] = list(features.ix[:,4].str.replace(":"," "))
features.ix[:,8] = list(features.ix[:,8].str.replace(":"," "))


#### to see whether more is better
    
for n in range(0, len(features)):    
    features.ix[n,4] = sum([1 for x in features.ix[n,4].split()])
    features.ix[n,8] = sum([1 for x in features.ix[n,8].split()])
    if features.ix[n,3] == '10+':
        features.ix[n,3] = 10
    elif features.ix[n,3] != '10+':
        features.ix[n,3] = features.ix[n,3]
    if features.ix[n,7] == '10+':
        features.ix[n,7] = 10
    elif features.ix[n,7] != '10+':
        features.ix[n,7] = features.ix[n,7]
  

  
features.ix[:,0] = pd.Categorical(features.ix[:,0]).codes
features.ix[:,1] = pd.Categorical(features.ix[:,1]).codes
features.ix[:,5] = pd.Categorical(features.ix[:,5]).codes
features.ix[:,6] = pd.Categorical(features.ix[:,6]).codes
features.ix[:,9] = pd.Categorical(features.ix[:,9]).codes


pd.plotting.scatter_matrix(features,alpha=0.2, figsize=(10, 10), diagonal='kde')
plt.show()



X_train, X_test, y_train, y_test = train_test_split(selected_features, grades, test_size = 0.25, random_state = 1000)

########### snippet taken from https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py
 


def benchmark(clf): 
    clf.fit(X_train, y_train.values.ravel())
    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print("test time:  %0.3fs" % test_time)
    score = metrics.accuracy_score(y_test, pred)
    print("accuracy:   %0.3f" % score)
    return score


results = []

# Train Liblinear model
results.append(benchmark(LinearSVC(tol=1e-3)))

# Train SGD model
results.append(benchmark(SGDClassifier(alpha=.0001, max_iter=50,)))

# Train SGD with Elastic Net penalty
print("Elastic-Net penalty")
results.append(benchmark(SGDClassifier(alpha=.0001, max_iter=50,
                                       penalty="elasticnet")))

# Train NearestCentroid without threshold

print("NearestCentroid (aka Rocchio classifier)")
results.append(benchmark(NearestCentroid()))

# Train sparse Naive Bayes classifiers

print("Naive Bayes")
results.append(benchmark(MultinomialNB(alpha=.01)))
results.append(benchmark(BernoulliNB(alpha=.01)))
results.append(benchmark(ComplementNB(alpha=.1)))
