from ursina import *
from random import uniform

app = Ursina()
window.color = color.lime
EditorCamera()

# ----- 필드, 골대, 공 생성 -----
field = Entity(model='plane', texture='grass', scale=(30, 1, 50), color=color.green)
goal_post = Entity(model='cube', color=color.white, scale=(6, 4, 0.2), position=(0, 2, 25))
crossbar = Entity(model='cube', color=color.white, scale=(6, 0.2, 0.2), position=(0, 4, 25))
goal_left = Entity(model='cube', color=color.white, scale=(0.2, 4, 0.2), position=(-3, 2, 25))
goal_right = Entity(model='cube', color=color.white, scale=(0.2, 4, 0.2), position=(3, 2, 25))

ball = Entity(model='sphere', color=color.white, scale=1, position=(0, 1, -15), collider='sphere')
score_text = Text(text='Score: 0', position=(-.85, .45), scale=2, color=color.black)

# ----- 변수 설정 -----
speed = Vec3(0, 0, 0)
gravity = -9.8
in_air = False
score = 0

def input(key):
    global speed, in_air
    # 스페이스바로 공을 찬다 (포물선)
    if key == 'space' and not in_air:
        in_air = True
        speed = Vec3(uniform(-1, 1), 6, 25)  # 방향, 높이, 거리

def update():
    global speed, in_air, score

    # 공의 움직임
    if in_air:
        speed.y += gravity * time.dt
        ball.position += speed * time.dt

        # 바닥 닿으면 멈추기
        if ball.y <= 1:
            ball.y = 1
            speed = Vec3(0, 0, 0)
            in_air = False

        # 골대와 충돌 시 골 판정
        if (abs(ball.x) < 2.5 and 0.5 < ball.y < 3.5 and 24.5 < ball.z < 25.5):
            score += 1
            score_text.text = f'Score: {score}'
            print('GOAL!')
            goal_post.color = color.yellow
            invoke(reset_ball, delay=1)


def reset_ball():
    global ball, in_air
    ball.position = (0, 1, -15)
    in_air = False
    goal_post.color = color.white

app.run()
