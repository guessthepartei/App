import os, os.path
import random
# import parse.py
import subprocess
from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

partys = os.listdir("dataset")
partys.remove(".DS_Store")

#print(partys) 

party = random.choice(partys)


print(party)
plakats = os.listdir('dataset/{}'.format(party))
#print(plakats)

plakat = random.choice(plakats)
#print(plakat)


os.system("python3 parsing.py {}/{}".format(party, plakat))
