from ursina import *

app = Ursina()

def on_button_click():
    print('버튼 클릭!')

btn = Button(text='Click me', color=color.azure, scale=.2, parent=camera.ui, position=(-.7, .4))
btn.on_click = on_button_click

app.run()
