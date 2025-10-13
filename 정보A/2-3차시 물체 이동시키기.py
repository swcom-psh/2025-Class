from ursina import *
import random as ran

app = Ursina()
EditorCamera()

objects = 2000
somethings = []

def input(key):
    if key == 'escape':
        application.quit()

for i in range(objects):
    pos = (ran.uniform(-100,100), ran.uniform(-100,100), ran.uniform(-100,100))#튜플 이라고 하는 자료형
    a = Entity(
        model = 'sphere',
        color = color.random_color(),
        position = pos,
        scale = 5
    )
    a.dis = Vec3(ran.uniform(-10,10), ran.uniform(-10,10), ran.uniform(-10,10))#튜플 이라고 하는 자료형 
    somethings.append(a)
    
height = 100

def update():#예약함수 중 하나로, 1초에 60프레임// 1초에 60회 반복해주는 함수
    for some in somethings:
        some.position += some.dis
        #some.position = some.position + ~~
        if abs(some.x) + abs(some.z) > (height - some.y) or a.y < 0 or a.y > height:
            some.dis *= -1
    
        

app.run()

