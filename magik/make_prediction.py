import pickle
import sys

documents = ['ich moechte dass mein sohn richtig deutsch sprechen lernt weil das die voraussetzung ist zu einem guten beruf die nimmt das schulwesen ernst und deshalb waehle ich sie unbequem echt mutig ', 'damit es beim naechsten karneval der kulturen nicht wieder zu uebergriffen auf frauen kommt waehle ich diesmal die das mit der armlaenge abstand haut einfach nicht hin unbequem echt mutig ', 'fuer unser land fuer unsere werte verstand statt ideologie im landtag ', 'asylantenattacke in regensburg kriminelle asylbewerber muessen unverzueglich abgeschoben werden ', 'sicherheit freiheit wohlstand ', 'mein partner und ich legen keinen wert auf die bekanntschaft mit muslimischen einwanderern fuer die unsere liebe eine todsuende ist unbequem echt mutig ', 'freiheit gleichheit schwester lichkeit kommt wir bauen das neue europa ', 'nur ein soziales europa ist ein starkes europa kommt wir bauen das neue europa ', 'europa ist ein friedensprojekt kein steuer wir bauen das neue europa ', 'kommt der mut geht bauen das netr europa ', 'klima schutz kennt keine grenze kommt wir bauen das neue europa ', 'perfekt ist europa nicht aber ein verdammt guter start wir das', 'geld bildung statt fuer bonzen ', 'europa die beste idee die europa je hatte kommt wir bauen das neue europa ', 'wer den planeten retten will faengt mit diesem kontinent an wir bauen das neue', 'fuer koenigin auf unseren wiese kommt wir bauen das neue europa ', 'eine mutige geseflschaft laesst sich keine angst machen kommt wir bauen das neue europa ', 'gleicher lohn fuer gleiche und gleichwertige arbeit ', 'stoppt die afd antworten auf die gefahr von rechts ', 'endlich straffrei kiffen ', 'soziale stadt fuer alle lust auf kommunalpolitik ales veraendert sich wenn du es veraenderst rio reiser ton steine scherben ', 'ruestung exporte verbieten', 'streik fuer eine zukunft fuer die sich ', 'nur solidarisch', 'amazon pay ', 'wirr ist das volk ', 'voellig sinnlos eine pyramide fuer bremen fuenf stimmen fuer null versprechen', 'waehlt wer von euch wusste vor fuenf jahren dass das eu parlament ein mal im monat fuer zirka 15 millionen uro mtl von bruessel nach strassburg umzieht und damit pro jahr etwa 20 tausend tonnen c02 produziert europawah12019 sonnebornrettetdieeu', 'herr bleibt bruessel noch mehr abenteuer im europaparlament sonjneb0rn semsrott 2019 fuer europa reicht ', 'proletarier aller laender vereinigt euch konsequent ', 'protest ist links konsequent ', 'fuer das recht auf flucht konsequent ', 'gegen imperialistische aggression konsequent ', 'mach mit damit sich wirklich etwas aendert konsequent ', 'hoch die internationale solidaritaet long live international solidarity konsequent ', 'azadi bo freiheit fuer kurdistan konsequent ', 'buerger muessen mitredenfreie und buergerstadt hamburg', 'bezahlbare mietwohnungen schaffen zukunft jetzt machen', ' europaistdieantwort', 'unsere schulen modernisieren tsg18 zukunft jetzt machen', 'klimaschutz europaistdieantwort', 'rainer troeger ein soziales guntersblum unser buergermeisterkandidat', ' europaistdieantwort', 'stadt und land besser verbinden tsg18 zukunft jetzt machen', ' europaistdieantwort', 'kueken mord verbieten jedes jahr werden in ueber 40 millionen kueken direkt nach der geburt getoetet nur weil sie maennlich sind und keine eier legen mehr unter ehrliche politik fuer alle ', 'hunde rassenliste abschaffen denn rassismus ist falsch egal ob bei mensch oder tier und kampf hunde entstehen durch training nicht rasse', 'meine mama und ich fuer ihr hobby jaehrlich toeten ca 350 000 jaeger etwa 10 millionen wildtiere mitgefuehl waehlen ', 'massen tierhaltung abschaffen ehrliche politik fuer alle ']

with open('text_classifier', 'rb') as training_model: 
   model = pickle.load(training_model)
from sklearn.feature_extraction.text import TfidfVectorizer
    
from sklearn.feature_extraction.text import TfidfTransformer
#X = sys.argv[1]
X = ["Mach mit! Damit sich wirklich etwas ändert Konsequent. Internationalistische Liste"]

import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context



nltk.download()
#nltk.download('stopwords')
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer(max_features=5, min_df=5, max_df=0.7, stop_words=stopwords.words('german'))
#X = vectorizer.fit_transform(documents).toarray()

#print(X)


from sklearn.feature_extraction.text import TfidfTransformer
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

print(X)
y = model.predict(X)

print(y)




