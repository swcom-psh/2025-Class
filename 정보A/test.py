from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

__ = False

app = Ursina()
EditorCamera()

#player = FirstPersonController(speed = 20)



def input(key):
    if key == 'escape':
        application.quit()  

wall = [
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,__,__,13,14,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,__,__,__,14,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,__,15,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,__,16,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,15,__,17,18,19,20],
    [11,21,31,41,51,61,71,81,91,10,11,__,13,14,15,16,17,18,19,20]
]

for i in range(len(wall)): #i는 행의 개수를 의미 >> 5
    for j in range(len(wall[i])): #j는 열의 개수를 의미 >> 10
        if wall[i][j]: #i, j 인자를 주소로 리스트 값에 접근해 T/F 판단
            test = Entity(
                model = 'cube',
                texture = 'brick',
                color = '#d1a432',
                scale = 5,
                position = (i * 5,0,j * 5),
                collider = 'box' #충돌 감지
            )
        else:
            test = Entity(
                model = 'cube',
                texture = 'brick',
                color = "#ffffff",
                scale = 5,
                position = (i*5, 0, j*5)
            )


ground = Entity(
    model = 'plane',
    scale = (1000,1,1000),
    position = (0,-3,0),
    texture='grass',
    collider = 'box' #충돌 감지
)

tt = Entity(
    model = 'plane',
    scale = (10,1,10),
    rotation = (270,0,0),
    position = (0,25,5),
    texture = 'assets/다운로드.jpg'
)

tttt = Text(
    text = 'Hello',
    scale = 5,
    position = (0,0.4),
    origin = (0,0) #좌표
)




app.run()
