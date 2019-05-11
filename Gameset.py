from utils import json_load
class Gameset(object):

    def __init__(self, id):
        self.base = "data/processed/" + str(id)
        self.text = open(self.base + "text.txt", "r").read()
        self.meta = json_load(self.base + "/meta.json")

    def get_text(self):
        return self.text

    def get_party(self):
        return self.meta["party-name"]

    def get_poster_path(self):
        return self.base + "poster.png"

    def get_solution_path(self):
        return self.base + "solution.png"
