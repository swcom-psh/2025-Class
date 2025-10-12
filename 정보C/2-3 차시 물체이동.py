from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.
import random as ran


app = Ursina()
EditorCamera()

objects = 300

somethings = []

def input(key):
    if key == 'escape':
        application.quit()

for obj in range(objects):
    pos = Vec3(ran.uniform(-100,100), 0, ran.uniform(-100,100))

    cube = Entity(
        model = 'sphere', #속성
        position = pos,
        scale = 5,
        color = color.random_color()
    )
    cube.dirs = Vec3(ran.uniform(-10,10), 0, ran.uniform(-10,10))
    #큐브 객체의 dirs 속성을 만들어주었다.
    #우르시나에서만 쓰는 자료형: Vec3 >> 벡터형태의 3차원(x,y,z 좌표)자료형

    somethings.append(cube) #큐브 객체를 썸띵리스트에 저장
    #각 엔티티의 정보가 담기겠죠.

def update():
    for some in somethings:
        some.position += some.dirs * time.dt

        if abs(some.x) > (some.x)*(some.x) + (some.z)*(some.z): #abs() 절대값을 출력해주는 함수
            some.dirs.x *= -1
        if abs(some.z) > (some.x)*(some.x) + (some.z)*(some.z): #abs() 절대값을 출력해주는 함수
            some.dirs.z *= -1   



    




app.run()