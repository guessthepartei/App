import pickle

def predict(sen):
   with open('my_dumped_classifier.pkl', 'rb') as fid:
      clf = pickle.load(fid)
   sent = [sen]
   print(clf.predict(sent))
   return(clf.predict(sent).item(0))
