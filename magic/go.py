import os, os.path
import parsing
import random
import json
# import parse.py
import subprocess
import predict
from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def go():
   partys = os.listdir("dataset")
   partys.remove(".DS_Store")

#print(partys)

   party = random.choice(partys)


   #print(party)
   plakats = os.listdir('dataset/{}'.format(party))
#print(plakats)

   plakat = random.choice(plakats)
   #print(plakat)
   #print(parsing.parsing("{}/{}".format(party, plakat)))
   print()
   link = "dataset/{}/{}".format(party, plakat)
   text = parsing.parsing("{}/{}".format(party, plakat))
   pred = predict.predict(text)
   x = {
      "link": link,
      "text": text,
      "party": party,
      "predict": pred
    }

   return json.dumps(x)
#os.system("python3 parsing.py {}/{}".format(party, plakat))


if __name__ == "__main__":
    main()
