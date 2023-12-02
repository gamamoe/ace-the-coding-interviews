import sys; input = sys.stdin.readline
N, M = map(int, input().split())
mtxA = [list(map(int, input().split())) for _ in range(N)]
mtxB = [list(map(int, input().split())) for _ in range(N)]
# 생성될 새로운 행렬
matrix = [[0]*M for _ in range(N)]

# 행렬 더하기
for i in range(N):
    for j in range(M):
        matrix[i][j] = mtxA[i][j] + mtxB[i][j]

# 여러 줄에 걸쳐서 출력하기
for k in matrix:
    print(' '.join(map(str, k)))