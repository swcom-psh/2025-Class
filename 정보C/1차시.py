from ursina import *
#우르시나 라이브러리의 모든 기능(=*)을 가져온다.

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

cube = Entity(model = 'cube',position = (0, 0, 0), scale = 5, color = '#37aa29')
cube = Entity(model = 'sphere',position = (0, 10, 0), scale = 5, color = '#37aa29')
cube = Entity(model = 'plane',position = (0, 20, 0), scale = 5, color = '#37aa29')



app.run()
