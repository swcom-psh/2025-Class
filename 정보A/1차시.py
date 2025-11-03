from ursina import *

app = Ursina()
EditorCamera()


def input(key):
    if key == 'escape':
        application.quit()

cube = Entity(model = 'cube', scale = 5, position = (0,0,0), color = color.red, blink = True)

app.run()

