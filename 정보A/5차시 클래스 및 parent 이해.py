from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

class Planet(Entity):
    def __init__(self, name, texture, position, scale, rotation_speed):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = position,
            scale = scale,
            rotation_speed = rotation_speed
        )
        self.name = name

    def update(self):
        self.rotation_y += self.rotation_speed * time.dt

sun_texture = load_texture('textures/sun.jpg')


Planet('Sun', sun_texture, (3,0,0), (5, 5, 5), 47.87)

app.run()
