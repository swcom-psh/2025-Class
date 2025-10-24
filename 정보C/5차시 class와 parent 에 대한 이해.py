from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

class Planet(Entity): ## 행성을 만드는 클래스를 선언한다.
    def __init__(self, texture, pos, scale):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = pos,
            scale = scale
        )

Planet(texture = 'textures/sun.jpg', pos = (0, 0, 0), scale = 5)
Planet(texture = 'textures/earth.jpg', pos = (5, 0, 0), scale = 5)
Planet(texture = 'textures/mars.jpg', pos = (10, 0, 0), scale = 5)








app.run()
