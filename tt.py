from ursina import *
app = Ursina()
player = Entity(model='cube', color=color.green, scale=1, collider='box', position=(0,1,0))
ground = Entity(model='plane', color=color.gray, scale=(10,1,10), collider='box', position=(0,0,0))

def input(key):
    if key == 'space':  # 만약 스페이스바가 눌렸다면
        player.y += 2  # 플레이어를 위로 점프시킴

app.run()