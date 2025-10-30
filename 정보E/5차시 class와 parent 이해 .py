from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.

app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


class Planet(Entity):
    def __init__(self, tex, sc, pos, spin, orbit):
        super().__init__(
            model = 'sphere',
            texture = tex,
            scale = sc,
            position = pos,
            spin = spin,
            orbit = orbit
        )
        self.pivot()
    
    def pivot(self):
        self.pi = Entity(position = (0,0,0))
        self.parent = self.pi

        
    def update(self):
        #self는 클래스 내부에서 생성되는 변수 등을
        #클래스 자기자신 내부에서 접근하기 위함
        self.rotation_y += self.spin
        self.pi.rotation_y += self.orbit





earth = Planet(tex = 'textures/earth.jpg', sc = 5, pos = (0,0,0), spin = 5, orbit = 5)
sun = Planet(tex = 'textures/sun.jpg', sc = 5, pos = (10,0,0), spin = 150, orbit = 0)




app.run()


