from ursina import *
app = Ursina()
EditorCamera()
player = Entity(model='cube', color=color.green, scale=1, collider='box', position=(0,1,0))
ground = Entity(model='plane', color=color.gray, scale=(10,1,10), collider='box', position=(0,0,0))
def update():
    if player.y > 1:  # 플레이어가 땅 위에 있을 때만 중력 적용
        player.y -= 0.1  # 중력 효과로 플레이어를 아래로 이동
    if player.intersects(ground).hit:  # 플레이어가 땅과 충돌했을 때
        player.y = 1  # 플레이어를 땅 위에 고정

app.run()