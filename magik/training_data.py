import os, os.path
import parsing

result = []

partys = ["AfD", "Die_Gruene", "Die_Linke", "Die_Partei", "MLPD", "Piratenpartei", "SPD", "Tierschutzpartei"]

for party in partys:
   dict = {party:[]}
   print(party)
   for plakat in os.listdir("dataset/{}".format(party)):
      dict.get(party).append(parsing.parsing("{}/{}".format(party, plakat)))
   print(dict)
   result.append(dict)
