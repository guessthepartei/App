import numpy as np  
import re  
from sklearn.datasets import load_files  
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


documents = []

for sen in range(0, len(X)):  
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))

    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 

    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    document = re.sub(r'[üÜ]', 'ue', document, flags=re.I)
    document = re.sub(r'[öÖ]', 'oe', document, flags=re.I)
    document = re.sub(r'[äÄ]', 'ae', document, flags=re.I)
    document = re.sub(r'[ß]', 'ss', document, flags=re.I)
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # Converting to Lowercase
    document = document.lower()

    documents.append(document)

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.feature_extraction.text import TfidfTransformer  
tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=[' ', ',', '.'])
X = tfidfconverter.fit_transform(documents).toarray()  


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=1000, random_state=0)  
classifier.fit(X_train, y_train)  

y_pred = classifier.predict(X_test)  


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  
print(accuracy_score(y_test, y_pred))  


with open('text_classifier', 'wb') as picklefile:  
    pickle.dump(classifier,picklefile)



with open('text_classifier', 'rb') as training_model:  
    model = pickle.load(training_model)


y_pred2 = model.predict(X_test)

print(confusion_matrix(y_test, y_pred2))  
print(classification_report(y_test, y_pred2))  
print(accuracy_score(y_test, y_pred2))  
