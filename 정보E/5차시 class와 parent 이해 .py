from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.

app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


class Planet(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texutre = '',
            scale = 5,
            position = (0,0,0)
        )

        


Planet()



earth = Entity(model = 'sphere', texture ='textures/earth.jpg', scale = 5, position = (0,0,0))
earth = Entity(model = 'sphere', texture ='textures/earth.jpg', scale = 5, position = (0,0,0))
earth = Entity(model = 'sphere', texture ='textures/earth.jpg', scale = 5, position = (0,0,0))
earth = Entity(model = 'sphere', texture ='textures/earth.jpg', scale = 5, position = (0,0,0))

def update(): #업데이트 라는 함수
    #이 안에 있는 코드는 프로그램 실행 후 무한 반복됨.
    earth.rotation_y += 5
    #earth.rotation_y = earth.rotation_y + 5
    earth.position += Vec3(0.5, 0, 0)




app.run()


