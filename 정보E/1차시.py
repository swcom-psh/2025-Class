from ursina import * #우르시나 라이브러리로부터 모든 기능을 가져온다.

app = Ursina() #app이라는 객체에 우르시나 월드를 불러온다.
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


cube = Entity(model = 'cube', scale = 5, position = (0,0,0), color = color.red)




app.run()


