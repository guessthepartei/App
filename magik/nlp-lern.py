import numpy as np 
import re 
import pickle 
import json

data = open("train_set", "r").read()

data = json.loads(data)
X = []
y = []

for party in data:
   for plakat in data.get(party):
      X.append(plakat)
      y.append(party)

import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


# The training data folder must be passed as first argument

# Split the dataset in training and test set:
docs_train, docs_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)


# TASK: Build a vectorizer that splits strings into sequence of 1 to 3
# characters instead of word tokens
vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char',
                             use_idf=False)

# TASK: Build a vectorizer / classifier pipeline using the previous analyzer
# the pipeline instance should stored in a variable named clf
clf = Pipeline([
    ('vec', vectorizer),
    ('clf', Perceptron(tol=1e-3)),
])

# TASK: Fit the pipeline on the training set
clf.fit(docs_train, y_train)

# TASK: Predict the outcome on the testing set in a variable named y_predicted
y_predicted = clf.predict(docs_test)


# Plot the confusion matrix
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)

sentences = [
    'This is a language detection test.',
    'Ceci est un test de d\xe9tection de la langue.',
    'Dies ist ein Test, um die Sprache zu erkennen.',
]
predicted = clf.predict(sentences)

print(predicted)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_predicted)) 
print(classification_report(y_test,y_predicted)) 
print(accuracy_score(y_test, y_predicted)) 

import pickle
with open('my_dumped_classifier.pkl', 'wb') as fid:
    pickle.dump(clf, fid)    

import pickle
s = pickle.dumps(clf)

