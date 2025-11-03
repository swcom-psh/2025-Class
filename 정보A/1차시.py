from ursina import *

app = Ursina()
EditorCamera()


def input(key):
    if key == 'escape':
        application.quit()

cube = Entity(model = 'cube', scale = 5, position = (0,0,0), color = color.red, blink = True)

Button(
    text='HI', 
    parent=camera.ui, 
    model=Default, 
    radius=Default, 
    origin=(0, 0), 
    texture=Default, 
    color=Default, 
    collider='box', 
    text_color=Default, 
    text_origin=(0, 0), 
    text_size=1, 
    highlight_text_size=None, 
    highlight_text_color=None, 
    highlight_scale=1, 
    pressed_scale=1, 
    disabled=False
    )



app.run()

