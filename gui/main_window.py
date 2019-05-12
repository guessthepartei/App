from guizero import App, Text, Picture, PushButton

from gui.guizero import Box


class Gui(object):
    # text, picture = {}
    buttons = []

    # app = {}

    # The class "constructor" - It's actually an initializer
    def __init__(self, text, picture):
        self.app = App(title="guessthepartei")
        # self.app.on_close(exit(0))
        # self.game = game
        self.statusbox = Box(self.app, layout="grid", border = 1)
        self.status = Text(self.statusbox, text="wrong", width=33, height=5, grid=[1, 0])
        self.next_btn = PushButton(self.statusbox, command=next, width=34, grid=[2, 0], text='Next', align='center')
        self.scoretext = Text(self.statusbox, text="Score: ", width=33, height=5, grid=[0, 0])
        self.text = Text(self.app, text=text, height=7)
        self.buttonbox = Box(self.app, layout="grid")
        self.add_buttons()
        Box(self.app, height=10, width=100, layout='grid')
        self.picture = Picture(self.app, image=picture)
        self.app.display()

    def add_buttons(self):
        parties = ['AfD', 'Gruene', 'Die Linke', 'Die Partei', 'MLPD', 'Piraten', 'SPD', 'Tierschutzpartei']
        for i in range(len(parties)):
            name = parties[i]
            self.buttons.append(PushButton(self.buttonbox, command=self.btn_handler, grid=[i % 4, i // 4], text=name,
                                           width=15, height=5, args=[name]))

    def set_picture(self, picture):
        self.picture.set(picture)

    def set_text(self, text):
        self.text.clear()
        self.text.append(text)

    def close(self):
        self.app.destroy()

    def btn_handler(self, party_name):
        print(party_name)


def make_gui(text, picture):
    return Gui(text, picture)


make_gui('Guess the Partei', 'images/baum.png')
