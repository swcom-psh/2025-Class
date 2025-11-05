from ursina import *
import random as rd

app = Ursina()
EditorCamera()


def input(key):
    if key == 'escape':
        application.quit()


count = []


class Quiz(Entity):
    def __init__(self,tex, pos):
        super().__init__(
            model='plane',
            texture=tex,
            scale=(2, 2, 2),
            rotation = (270,0,0),
            position= pos,
            collider = 'box' #클릭을 구현하려면 반드시 충돌체가 있어야함.
        )
        self.real = tex  ##정답~
        self.fake = 'quiz/뒷면.png' ##뒷면~
        invoke(self.flip, delay=3)  ## 이 코드 실행하고나서 3초 뒤에 flip 함수 실행해라~ >> 카드 다시 뒷면으로 뒤집기 3초뒤에
    
    def flip(self): #뒷면으로 바꾸는 함수
        self.texture = self.fake

    def unflip(self): #앞면으로 바꾸는 함수
        self.texture = self.real
             

    def on_click(self): #우르시나에서는 update 처럼 클릭했을 때 실행되는 함수가 on_click 이다~~~
        global count
        self.unflip()
        count.append(self)

        if len(count) == 2:
            if count[0].real == count[1].real:
                print("맞췄습니다!")
                for card in count:
                    destroy(card)
            else:
                print("틀렸습니다!")
                for card in count:
                   invoke(card.flip, delay=1) #1초 뒤에 다시 뒤집기
            count = []
        


quiz_texture = ['quiz/문제1.png', 'quiz/문제2.png', 'quiz/문제3.png', 'quiz/문제4.png', 'quiz/문제5.png', 'quiz/문제6.png', 'quiz/문제7.png', 'quiz/문제8.png', 'quiz/문제1.png', 'quiz/문제2.png', 'quiz/문제3.png', 'quiz/문제4.png', 'quiz/문제5.png', 'quiz/문제6.png', 'quiz/문제7.png', 'quiz/문제8.png']
#퀴즈도 16개
rd.shuffle(quiz_texture) #리스트 랜덤하게 섞기
#참고: https://supermemi.tistory.com/entry/Python-3-random-%EB%AA%A8%EB%93%88-random-uniform-randint-randrange-choice-sample-shuffle

# 4x4 그리드의 위치 리스트 (좌->우, 위->아래)
positions = [ #16개
    (-4, 4, 0), (-2, 4, 0), (0, 4, 0), (2, 4, 0),
    (-4, 2, 0), (-2, 2, 0), (0, 2, 0), (2, 2, 0),
    (-4, 0, 0), (-2, 0, 0), (0, 0, 0), (2, 0, 0),
    (-4, -2, 0), (-2, -2, 0), (0, -2, 0), (2, -2, 0),
]

quiz = []

for tex, pos in zip(quiz_texture, positions): #각각의 텍스쳐와 위치를 쌍으로 묶어서 tex, pos 반복변수로 반복하기.
    quiz.append(Quiz(tex, pos))

app.run()

