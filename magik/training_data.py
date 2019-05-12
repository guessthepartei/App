import os, os.path
import parsing

result = []

partys = ["AfD", "Die Gruene", "Die Linke", "Die Partei", "MLPD", "Piratenpartei", "SPD", "Tierschutzpartei"]

for party in partys:
   dict = {party:[]}
   print(party)
   for plakat in os.listdir("dataset/{}".format(party)):
      dict.get(party).append(parsing.parsing("{}/{}".format(party, plakat)))
   print(dict)
   result.append(dict)
