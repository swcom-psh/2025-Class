from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

player = FirstPersonController(
    speed = 200,
    jump_height = 50
)

def input(key):
    if key == 'escape':
        application.quit()

#cube = Entity(model = 'cube',position = (0, 0, 0), scale = 5, color = '#37aa29')

ground = Entity(model = 'plane', scale = (1000,0,1000), collider = 'box',position = (0, -5, 0), texture = 'assets/잔디밭.jpg')

album = Entity(model = 'plane', scale = (20,0,20),position = (0, 10, 0), rotation = (270,0,0), texture = 'assets/사진1.jpg')


Sky(texture = "sky_sunset")


app.run()
