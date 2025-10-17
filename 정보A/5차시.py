from ursina import *

app = Ursina()
EditorCamera()


def input(key):
    if key == 'escape':
        application.quit()


earth = Entity(model = 'sphere', texture = 'textures/earth.jpg', scale = 5, position = (0,0,0))
sun = Entity(model = 'sphere', texture = 'textures/sun.jpg', scale = 5, position = (10,0,0))


class Planet(Entity):
    def __init__(self, texture, position, a):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = position,
            scale = a,
        )
        
Planet(texture = 'textures/earth.jpg', position = (20,0,0), a = 5)
# 수성 
# 금성
# 





app.run()

