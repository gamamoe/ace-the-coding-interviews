import sys; input = sys.stdin.readline
mtx = [list(map(int, input().split())) for _ in range(9)]
#비교 대상 리스트
compare = []
for i in range(9):
    for j in range(9):
        compare.append(mtx[i][j])
print(maximum:= max(compare))
#divmod(A, B) 의미: A / B의 (몫, 나머지) tuple로 출력
# 행, 열 반환을 원하면 divmod(max_index, num_cols) 사용
row, col = divmod(compare.index(maximum), 9)
#몫 = row, 나머지 = col  -> 인덱스 +1 반영
print(row+1, col+1)