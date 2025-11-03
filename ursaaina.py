from ursina import *

app = Ursina()
EditorCamera()


cube = Entity(model = 'cube', scale = 5, position = (0,0,0), color = color.red, collider='box')
ball = Entity(model='sphere', scale=2, position=(2,5,0), color=color.blue, collider='sphere')

cube.animate('y', 3, duration=1) # y축으로 3만큼 올라가는 애니메이션

cube.animate_rotation((0,180,0), duration=2) # y축으로 180도 회전하는 애니메이션
cube.shake(magnitude=2, duration=10) # 흔들리는 애니메이션

if cube.intersects().hit:
    print('충돌!')

app.run()

