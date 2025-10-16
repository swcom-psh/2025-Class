from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

sun_texture = load_texture('textures\sun.jpg')


sun = Entity(
    model = 'sphere',
    texture = sun_texture,
    color = color.white,
    scale = 5,
    position = (0,0,0)
)



app.run()
