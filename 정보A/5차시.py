from ursina import *
app = Ursina()
EditorCamera()
def input(key):
    if key == 'escape':
        application.quit()
# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

class Planet(Entity):  # Planet의 부모는 Entity다
    def __init__(self, texture, position,a, speed, orbit = 0):#각 입력변수, 파라미터
        # super : 부모의 기능을 가져오겠다
        super().__init__(
            model = 'sphere',
            texture = texture,
            position = position,
            scale = a,
            speed = speed,
            parent = scene
            )
        self.orbit = orbit
        self.pivot()
        
        
    def pivot(self): #투명 객체
        self.pi = Entity(position = (0,0,0))    
        self.parent = self.pi

    
    def update(self):
        self.rotation_y = self.rotation_y + self.speed
        self.pi.rotation_y = self.pi.rotation_y + self.orbit


Planet(texture = 'textures/sun.jpg', position = (0,0,0), a = 5, speed = 10, orbit = 2.5)
Planet(texture = 'textures/Mercury.jpg', position = (10,0,0), a = 5, speed = 0.7, orbit = 3.5)
Planet(texture = 'textures/Venus.jpg', position = (20,0,0), a = 5, speed = 0.8, orbit = 5.5)
Planet(texture = 'textures/Earth.jpg', position = (30,0,0), a = 5, speed = 1.2)
Planet(texture = 'textures/Mars.jpg', position = (40,0,0), a = 5, speed = 2)
Planet(texture = 'textures/Jupiter.jpg', position = (50,0,0), a = 5, speed = 3.5)
Planet(texture = 'textures/Saturn.jpg', position = (60,0,0), a = 5, speed = 8.5)
Planet(texture = 'textures/Uranus.jpg', position = (70,0,0), a = 5, speed = 9.5)
Planet(texture = 'textures/Neptune.jpg', position = (80,0,0), a = 5, speed = 10)

app.run()