import os, os.path
import parsing
result = []

partys = ["AfD", "Die_Gruene", "Die_Linke", "Die_Partei", "MLPD", "Piratenpartei", "SPD", "Tierschutzpartei"]

for party in partys:
   dict = {party:[]}
   print(party)
   plakats = os.listdir("dataset/{}".format(party))
   if ".DS_Store" in plakats:
      plakats.remove(".DS_Store")
   
   for plakat in plakats:
      print(plakat)
      dict.get(party).append(parsing.parsing("{}/{}".format(party, plakat)))
   result.append(dict)
print(result)
