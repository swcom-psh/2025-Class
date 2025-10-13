# 고2 정규 수업용: 멘델 단일형질 Punnett 시뮬레이터 (Ursina)
# 준비: pip install ursina
from ursina import *
import random

# --- 기본 매핑 ---
PHENOTYPE_COLOR = {
    'AA': color.orange,  # 우성
    'Aa': color.orange,  # 우성
    'aA': color.orange,  # 우성(정규화 전)
    'aa': color.azure    # 열성
}
# 유전형 정규화 함수: 'aA' -> 'Aa'
def normalize(geno):
    return ''.join(sorted(geno, key=lambda x: x.islower()))

# 부모 유전형에서 가능한 배우자(allele) 리스트
def gametes(geno):
    # 'AA' -> ['A','A'] , 'Aa' -> ['A','a'] , 'aa' -> ['a','a']
    return [geno[0], geno[1]]

# 자식 한 명 생성 (부모1/2에서 무작위로 한 알렐씩)
def make_child(p1, p2):
    a = random.choice(gametes(p1))
    b = random.choice(gametes(p2))
    return normalize(a + b)

# 이론 비율 계산 (Punnett 2x2 표)
def theoretical_ratio(p1, p2):
    g1 = gametes(p1)
    g2 = gametes(p2)
    box = []
    for a in g1:
        for b in g2:
            box.append(normalize(a+b))
    # 4칸 중 각 유전형 개수
    total = len(box)
    counts = {'AA':0,'Aa':0,'aa':0}
    for g in box:
        if g == 'AA': counts['AA'] += 1
        elif g == 'aa': counts['aa'] += 1
        else: counts['Aa'] += 1
    # 퍼센트로 반환
    return {k: int(counts[k]/total*100) for k in counts}

class PunnettApp(Ursina):
    def __init__(self):
        super().__init__()
        window.title = 'Punnett Simulator - 단일형질 유전'
        window.color = color.hex('0f1224')

        # 상태
        self.p1 = 'Aa'
        self.p2 = 'Aa'
        self.counts = {'AA':0,'Aa':0,'aa':0}
        self.total = 0
        self.help_on = True

        # UI
        self.title = Text(text='Punnett (단일형질) 시뮬레이터', x=-.86, y=.46, color=color.cyan, scale=1.1)
        self.parents = Text(text='', x=-.86, y=.40, color=color.white)
        self.theory = Text(text='', x=-.86, y=.34, color=color.yellow)
        self.stats  = Text(text='', x=-.86, y=.28, color=color.azure)
        self.help   = Text(text='', x=-.86, y=-.35, color=color.rgba(230,230,230,230), scale=.85)

        # 자식 그리드 영역
        self.grid_parent = Entity(parent=camera.ui)
        self.cells = []  # 최근 16명 시각화
        self.draw_grid([])

        self.update_texts()

    # 4x4 그리드에 최근 16명의 표현형 표시
    def draw_grid(self, last16):
        for c in self.cells:
            destroy(c)
        self.cells.clear()
        n = 16
        cols = 8  # 가로 8칸: 한 번에 16명 찍으면 2줄로 보이게
        size = 0.04
        start_x, start_y = -0.1, .05
        for i in range(min(len(last16), n)):
            g = last16[i]
            colr = PHENOTYPE_COLOR.get(g, color.white)
            x = start_x + (i % cols)* (size*1.2)
            y = start_y - (i // cols)* (size*1.2)
            e = Entity(parent=camera.ui, model='quad', color=colr, position=(x,y), scale=(size, size))
            Text(parent=e, text=g, scale=.9, z=-0.1, y=0, color=color.black)
            self.cells.append(e)

    def update_texts(self):
        t = theoretical_ratio(self.p1, self.p2)
        self.parents.text = f'부모1: {self.p1}   부모2: {self.p2}'
        self.theory.text  = f'이론 비율  (AA/Aa/aa): {t["AA"]}% / {t["Aa"]}% / {t["aa"]}%'
        if self.total == 0:
            self.stats.text = '실험 비율  (AA/Aa/aa): -'
        else:
            aa = int(self.counts['AA']/self.total*100)
            Aa = int(self.counts['Aa']/self.total*100)
            aa_small = int(self.counts['aa']/self.total*100)
            self.stats.text = f'실험 비율  (AA/Aa/aa): {aa}% / {Aa}% / {aa_small}%   (총 {self.total}명)'
        if self.help_on:
            self.help.text = (
                '[조작]\n'
                '부모1: Q=AA, W=Aa, E=aa   |   부모2: U=AA, I=Aa, O=aa\n'
                'Enter: 자식 1명 생성,  Shift+Enter: 자식 16명 생성,  R: 초기화,  H: 도움말 토글'
            )
        else:
            self.help.text = ''

    def input(self, key):
        # 부모1 선택
        if key == 'q': self.p1='AA'
        if key == 'w': self.p1='Aa'
        if key == 'e': self.p1='aa'
        # 부모2 선택
        if key == 'u': self.p2='AA'
        if key == 'i': self.p2='Aa'
        if key == 'o': self.p2='aa'

        # 생성
        if key == 'enter':
            g = make_child(self.p1, self.p2)
            self.counts[g] += 1
            self.total += 1
            self.draw_grid([g])  # 최근 결과만 한 칸
        if held_keys['shift'] and key == 'enter':
            last16 = []
            for _ in range(16):
                g = make_child(self.p1, self.p2)
                self.counts[g] += 1
                self.total += 1
                last16.append(g)
            self.draw_grid(last16)

        # 기타
        if key == 'r':
            self.counts = {'AA':0,'Aa':0,'aa':0}
            self.total = 0
            self.draw_grid([])
        if key == 'h':
            self.help_on = not self.help_on

        self.update_texts()

if __name__ == '__main__':
    PunnettApp().run()
