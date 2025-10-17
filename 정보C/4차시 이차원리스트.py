from ursina import *


app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


map = [
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

print(len(map))
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]:
            wall = Entity(
                model = 'cube',
                texture = 'white_cube',
                scale = 10,
                color = "#de7229",
                position = (i * 10, 0, j * 10)
            )
        else:
            wall = Entity(
                model = 'cube',
                texture = 'white_cube',
                scale = 10,
                color = "#5dc93f",
                position = (i * 10, 0, j * 10)
                )

for i in range(len(map2)):
    for j in range(len(map2[i])):
        if map2[i][j]:
            wall = Entity(
                model = 'cube',
                texture = 'white_cube',
                scale = 10,
                color = "#de3394",
                position = (i * 10, 10, j * 10)
            )



app.run()

