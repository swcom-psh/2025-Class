from ursina import *

app = Ursina()
EditorCamera()



mouse.visible = True     # 기본값 True, False면 커서 숨김
mouse.locked = False     # True면 마우스 위치 고정

cube = Entity(model = 'cube', scale = 5, position = (0,0,0), color = color.red, collider='box')


def update():
    if mouse.hovered_entity == cube:
        cube.color = color.random_color()
    else:
        cube.color = color.white

app.run()