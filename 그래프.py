from ursina import *
import math

app = Ursina()
EditorCamera()

# 함수 정의 (예: y = x^2 / 4)
def f(x):
    return (x**2) / 4

# 그래프 점들
points = [Entity(model='quad', color=color.azure, scale=(0.1,0.1),
                 position=(x/2, f(x/2))) for x in range(-20, 21)]

# 이동하는 점
p = Entity(model='circle', color=color.red, scale=0.3, position=(0, f(0)))

# 접선용 선분
tangent = Entity(model='quad', color=color.orange, scale=(0.0001,0.0001))

def update_tangent(x0):
    y0 = f(x0)
    h = 0.1
    m = (f(x0+h) - f(x0-h)) / (2*h)  # 수치 미분
    # 접선 선분 두 점 설정
    x1, x2 = x0 - 3, x0 + 3
    y1 = y0 + m*(x1 - x0)
    y2 = y0 + m*(x2 - x0)
    
    # 선분을 quad로 표현
    cx, cy = (x1+x2)/2, (y1+y2)/2
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    angle = math.degrees(math.atan2(y2-y1, x2-x1))
    tangent.position = (cx, cy)
    tangent.scale = (length, 0.05)
    tangent.rotation_z = angle

def update():
    # 좌우 키로 점 이동
    if held_keys['a']:
        p.x -= 2 * time.dt
    if held_keys['d']:
        p.x += 2 * time.dt
    p.y = f(p.x)
    update_tangent(p.x)

update_tangent(0)
app.run()
