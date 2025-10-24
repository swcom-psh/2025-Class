from ursina import *
import math

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()

# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
class Planet(Entity):
    def __init__(self, texture, position, a, speed, orbit=0, name=''):
        super().__init__(
            model='sphere',
            texture=texture,
            position=position,
            scale=a,
            speed=speed,
            parent=scene
        )
        self.orbit = orbit
        self.name = name
        self.angle = random.uniform(0, 360)
        self.pivot()

    def pivot(self):
        self.pi = Entity(position=(0, 0, 0))
        self.parent = self.pi

    def update(self):
        # --- 공통 자전 ---
        self.rotation_y += self.speed * time.dt

        # --- 일반 행성은 원형 공전 ---
        if self.name != 'Mars':
            self.pi.rotation_y += self.orbit * time.dt

        # --- 화성만 타원 + 기울기 반영 ---
        else:
            self.angle += self.orbit * 5   # 공전 속도 조절
            a = 40                # 태양으로부터 평균 거리
            e = 0.0934            # 이심률
            b = a * (1 - e)       # 타원 단축 비율
            inc = math.radians(1.85)  # 궤도 기울기 (°→rad)

            # 타원 궤도 좌표 계산
            self.x = math.cos(math.radians(self.angle)) * a
            self.z = math.sin(math.radians(self.angle)) * b * math.cos(inc)
            self.y = math.sin(math.radians(self.angle)) * b * math.sin(inc)

# --------------------------
# 행성 생성
# --------------------------
Planet(texture='textures/sun.jpg', position=(0, 0, 0), a=5, speed=10, orbit=2.5, name='Sun')
Planet(texture='textures/Mercury.jpg', position=(10, 0, 0), a=5, speed=0.7, orbit=3.5, name='Mercury')
Planet(texture='textures/Venus.jpg', position=(20, 0, 0), a=5, speed=0.8, orbit=5.5, name='Venus')
Planet(texture='textures/Earth.jpg', position=(30, 0, 0), a=5, speed=1.2, orbit=7, name='Earth')
Planet(texture='textures/Mars.jpg', position=(40, 0, 0), a=5, speed=2, orbit=2, name='Mars')  # ★ 수정된 부분
Planet(texture='textures/Jupiter.jpg', position=(50, 0, 0), a=5, speed=3.5, orbit=8.5, name='Jupiter')
Planet(texture='textures/Saturn.jpg', position=(60, 0, 0), a=5, speed=8.5, orbit=9.5, name='Saturn')
Planet(texture='textures/Uranus.jpg', position=(70, 0, 0), a=5, speed=9.5, orbit=10.5, name='Uranus')
Planet(texture='textures/Neptune.jpg', position=(80, 0, 0), a=5, speed=10, orbit=11.5, name='Neptune')

app.run()


#https://blog.naver.com/notenter9/220798073644