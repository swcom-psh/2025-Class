from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

class Planet(Entity): ## 행성을 만드는 클래스를 선언한다.
    def __init__(self, texture, pos, scale, speed, orbit):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = pos,
            scale = scale,
            speed = speed,
            orbit = orbit
        )
        self.pivot()
    
    def pivot(self):
        self.pi = Entity(position = (0,0,0))
        self.parent = self.pi

    def update(self):
        self.rotation_y += self.speed
        self.pi.rotation_y += self.orbit

Planet(texture = 'textures/sun.jpg', pos = (0, 0, 0), scale = 5, speed = 50, orbit = 0)
Planet(texture = 'textures/earth.jpg', pos = (55, 0, 0), scale = 5, speed = 100, orbit = 10)
Planet(texture = 'textures/mars.jpg', pos = (105, 0, 0), scale = 5, speed = 200, orbit = 40)








app.run()
