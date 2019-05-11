from guizero import App, Text, Picture, PushButton

from gui.guizero import Box


class Gui(object):
    # text, picture = {}
    buttons = []
    # app = {}

    # The class "constructor" - It's actually an initializer
    def __init__(self, text, picture, buttons):
        self.app = App(title="guessthepartei")

        self.picture = Picture(self.app, image=picture)
        self.text = Text(self.app, text=text)
        print(buttons)
        self.buttonbox = Box(self.app, layout="grid")
        i = 0;
        for x in buttons:
            print(x)
            self.buttons.append(PushButton(self.buttonbox, command=x['command'], grid=[i, 0],  text=x['text']))
            i += 1
        self.app.display()

    def set_picture(self, picture):
        self.picture.set(picture)

    def set_text(self, text):
        self.text.clear()
        self.text.append(text)

    def close(self):
        self.app.destroy()

def make_gui(text, picture, buttons):
    return Gui(text, picture, buttons)
