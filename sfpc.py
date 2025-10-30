
row, col = map(int, input().split())
n = int(input())

lst = []

for i in range(row):
    row_list = []
    for j in range(col):
        row_list.append(0)
    lst.append(row_list)

lst = [[0 for i in range(col)] for i in range(row)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for a in range(x1, x2+1):
        for b in range(y1, y2+1):
            lst[a][b] += 1

for i in range(row):
    for j in range(col):
        lst[i][j] %= 2
        print(f'{lst[i][j]} ')


