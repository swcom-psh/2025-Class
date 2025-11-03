from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.
import random as rd

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

lst = []

for i in range(10):
    cube = Entity(model = 'assets/야구공.fbx',
                   texture = 'assets/baseball_03.jpg',
                     position = (i*50, 0, 0),
                       scale = 5)
    lst.append(cube)

def update():
    #lst[0]~lst[9]
    for i in lst:
        i.rotation_y += 5
        i.position += Vec3(-5,4,0)


app.run()
