from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

class Planet(Entity): ## 행성을 만드는 클래스를 선언한다.
    def __init__(self, texture, pos, scale, orbit = 5):
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = pos,
            scale = scale,
            orbit = orbit
        )
        self.pivot()

    def pivot(self, angle=25):
        self.pi = Entity(
            position = (0,0,0),
            rotation_x = angle
        )
        self.parent = self.pi
    

    def update(self):
        self.rotation_y += 20 * time.dt #행성의 자전 속도 설정
        self.pi.rotation_y += self.orbit #행성의 공전 속도 설정

Planet(texture = 'textures/sun.jpg', pos = (0, 0, 0), scale = 5)
Planet(texture = 'textures/earth.jpg', pos = (55, 0, 0), scale = 5)
Planet(texture = 'textures/mars.jpg', pos = (105, 0, 0), scale = 5)








app.run()
