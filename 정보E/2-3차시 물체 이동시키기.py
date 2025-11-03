from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.
import random as ran



app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

objects = 300
somethings = []
speed = 5


for i in range(objects):
    pos = (ran.uniform(-100,100), ran.uniform(-100,100), ran.uniform(-100,100))

    cube = Entity(model = 'sphere', scale = 5, position = pos, color = color.random_color())
    cube.dis = Vec3(ran.uniform(-10,10),ran.uniform(-10,10),ran.uniform(-10,10)) #벡터 형태의 3차원 자료형 // 우르시나에서 쓰는 자료형
    somethings.append(cube)


def update():
    for some in somethings:
        some.position = some.position + some.dis * speed * time.dt #렉을 좀 덜어내준다.
        
        if abs(some.x) > 100:
            some.dis.x = some.dis.x * -1
            #some.dis.x *= -1
        if abs(some.y) > 100:
            some.dis.y *= -1
        
        if abs(some.z) > 100:
            some.dis.z *= -1

        
        



        
        


app.run()


