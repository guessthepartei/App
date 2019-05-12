import os, os.path
import magik.parsing
import random
# import parse.py
import subprocess
from subprocess import PIPE, run
import re

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def main():
   partys = os.listdir("../magik/dataset")
   partys.remove(".DS_Store")

#print(partys) 

   party = random.choice(partys)


   print(party)
   plakats = os.listdir('../magik/dataset/{}'.format(party))
#print(plakats)

   plakat = random.choice(plakats)
   #print(plakat)

   return "../magik/dataset/{}/{}".format(party, plakat), magik.parsing.parsing("{}/{}".format(party, plakat)), party
#os.system("python3 parsing.py {}/{}".format(party, plakat))
