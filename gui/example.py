from gui.Gui import make_gui

def b1():
    print("button1 pushed")

def b2():
    exit(0)
    # gui.close()
    # print("button2 pushed")

gui = make_gui("hallo Menschen", "images/baum.png",[{"text" : "button1", "command": b1}, {"text" : "button2", "command": b2}])


