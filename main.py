from gui.Gui import make_gui
from Gameset import Gameset
from utils import json_load

meta = json_load("Data/Processed/meta.json")

print(meta["parties"])
print(meta["poster-count"])


buttonlist = []

for x in meta["parties"]:
    x = 0

set = Gameset(1)

gui = make_gui(set.get_text,set.get_poster_path())


def get_gui():
    return gui
