import sys; input= sys.stdin.readline
# 0 으로 이뤄진 100 사이즈의 전체 종이
paper = [[0]*100 for _ in range(100)]
# 입력부분
p_num = int(input())
black_paper = [list(map(int, input().split())) for _ in range(p_num)]


for i in range(10): # 행 (범위는 1, 11하거나 이렇게 10만 하거나)
    for j in range(10): # 열
        for k in range(p_num): # 검은종이 순회
            if paper[black_paper[k][0] + i][black_paper[k][1] + j] == 1:
                continue # 1이면 연산 패스
            else: # 나머지는 1 할당
                paper[black_paper[k][0] + i][black_paper[k][1] + j] = 1

print(sum(sum(row) for row in paper)) # 2차원 배열의 전체 합
# idea: 전체를 0의 배열로 보고 1을 집어넣는 방식으로 구현한 문제이다.