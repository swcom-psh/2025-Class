from ursina import *

app = Ursina()
EditorCamera()


ceiling = Entity(model='cube', scale=(20,0.1,10), position=(0,0,0), color=color.gray)

pivot = Entity(position=(0,0,0))        
L = 10                                  

rod = Entity(parent=pivot, model='cube',
             scale=(0.12, L, 0.12),
             origin_y=0.5,               # 윗끝이 회전 원점
             position=(0, 0, 0),
             color=color.azure)

ball = Entity(parent=pivot, model='sphere',
              scale=1.2,
              position=(0, -L, 0),
              color=color.white)


angle = 15                               # 초기 각도(도)


def update():
    global angle
    t = time.time()
    theta = angle * cos(sqrt(9.8/L) * t)   # 단진자의 각도(도)
    pivot.rotation_z = theta                  # 진자 회전

app.run()
