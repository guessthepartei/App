from gui.guimain import make_gui


def b1():
    print("button1 pushed")

def b2():
    print("button2 pushed")

gut = make_gui("hallo Menschen", "images/baum.png",[{"text" : "button1", "command": b1}, {"text" : "button2", "command": b2}])

