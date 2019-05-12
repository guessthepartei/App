from guizero import App, Text, Picture, PushButton

from gui.guizero import Box

from magik.main import main


class Gui(object):
    # text, picture = {}
    buttons = []

    # app = {}

    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.app = App(title="guessthepartei")
        # self.app.on_close(exit(0))
        # self.game = game
        self.score = 0
        self.statusbox = Box(self.app, layout="grid", border=1)
        self.next_btn = PushButton(self.statusbox, command=self.next, width=34, grid=[1, 0], text='Next')
        self.status = Text(self.statusbox, text="", width=30, height=5, grid=[0, 0])
        self.scoretext = Text(self.statusbox, text="Score: ", width=33, height=5, grid=[2, 0])
        self.text = Text(self.app, text="", height=7)
        self.buttonbox = Box(self.app, layout="grid")
        self.add_buttons()
        Box(self.app, height=10, width=100, layout='grid')
        self.init()
        self.picture = Picture(self.app, image=self.solution, visible=False, height=1000)
        self.app.display()

    def add_buttons(self):
        parties = ['AfD', 'Die_Gruene', 'Die_Linke', 'Die_Partei', 'MLPD', 'Piratenpartei', 'SPD', 'Tierschutzpartei']
        for i in range(len(parties)):
            name = parties[i]
            self.buttons.append(PushButton(self.buttonbox, command=self.btn_handler, grid=[i % 4, i // 4], text=name,
                                           width=15, height=5, args=[name]))

    def set_picture(self, solution):
        self.picture.set(solution)

    def update_score(self):
        self.scoretext.value = 'Score: ' + str(self.score)

    def set_text(self, text):
        self.text.clear()
        self.text.append(text)

    def close(self):
        self.app.destroy()

    def btn_handler(self, party_name):
        if party_name == self.party:
            self.status.set('Correct')
            self.score += 1
        else:
            self.status.set('Wrong')

        self.update_score()
        self.picture.image = self.solution
        self.picture.visible = True


    def next(self):
        self.solution, text, self.party = main()
        self.set_text(text)
        self.picture.visible = False

    def init(self):
        self.solution, text, self.party = main()
        self.set_text(text)
        self.update_score()


def make_gui():
    return Gui()




if __name__ == '__main__':
    make_gui()
