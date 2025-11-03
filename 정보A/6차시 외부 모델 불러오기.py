from ursina import *

app = Ursina()
EditorCamera()


def input(key):
    if key == 'escape':
        application.quit()

lst = []

for i in range(10):
    cube = Entity(model = 'assets/apple.fbx',
                texture = 'assets/apple_01.jpg',
                scale = 5,
                position = (i * 100,0,0)
                )
    lst.append(cube)

def update():
    #lst[0]~lst[9]
    for i in lst:
        i.rotation_y += 5 *time.dt

    '''cube.rotation_y += 5
    if cube.x < 2000:
        cube.position += Vec3(5,0,0)
    else:
        cube.position += Vec3(-5,0,0)'''


app.run()

