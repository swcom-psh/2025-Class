from ursina import *

app = Ursina()
EditorCamera()  

cube = Entity(model='cube', color=color.orange, collider='box', scale=5)


def input(key):
    if key == 'left mouse down':  # 마우스 왼쪽 버튼 눌렀을 때
        if mouse.hovered_entity == cube:
            cube.color = color.random_color()
            print('큐브 클릭! 색이 바뀜!')

    if key == 'left mouse down' and mouse.world_point: #마우스 클릭 지점에 물체
        Entity(model='cube', color=color.random_color(), position=mouse.world_point, scale=5)


app.run()   