from guizero import App, Text, Picture, PushButton


class Gui(object):
    # text, picture = {}
    buttons = []
    # app = {}

    # The class "constructor" - It's actually an initializer
    def __init__(self, text, picture, buttons):
        self.app = App(title="guessthepartei")
        self.text = Text(self.app, text=text)
        self.picture = Picture(self.app, image=picture)
        print(buttons)
        for x in buttons:
            print(x)
            self.buttons.append(PushButton(self.app, command=x['command'], text=x['text']))
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
