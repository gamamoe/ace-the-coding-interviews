import sys; input = sys.stdin.readline
# 비어있는 최대 문자열 통 5x15
mtx = [[] for _ in range(5)]
answer = ''

for i in range(5): # input값을 줄별로 list 정의(line)
    line = list(map(str, input().strip()))
    mtx[i] = line + [''] * (15 - len(line))
      #그리고 채워지지않은 나머지를 ''로 채움

for j in range(15): #이걸 밖에둬야 i가 먼저 순회된다.
    for i in range(5):
        if mtx[i][j] != '':
            answer += mtx[i][j]
        else:
            continue
print(answer)