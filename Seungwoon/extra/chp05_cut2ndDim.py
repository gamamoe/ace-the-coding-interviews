# 1차원 배열 만드는 조건을 먼저 구한다.
# mtx는 해당 행까지는 해당 행 숫자, 그 이후로는 +1된다.
def solution(n, left, right):
    mtx = [[1] * n for _ in range(n)]
    # mtx 값 채우기 (규칙찾아 구현하기)
    for i in range(n):
        for j in range(n):
            if i == j:
                mtx[i][j] = i + 1
            elif i > j:
                mtx[i][j] = i + 1
            elif i < j:
                mtx[i][j] = j + 1

    # 1차원으로 나열하기
    mtx_one = []
    for i in mtx:
        mtx_one += i
    answer = mtx_one[left:right + 1]

    return answer
## 시간초과로 망한 코드
'''
3x3 행렬일 때
(1,1) = 1 (1,2) = 2 (1,3) = 3
(2,1) = 2 (2,2) = 2 (2,3) = 3
(3,1) = 3 (3,2) = 3 (3,3) = 3
간단하게 각 좌표 x, y 값중 큰 값이 해당 값이 됩니다.
이제 주어지는 left ~ right 1차원 index 값을, 2차원 인덱스(x, y) 값으로 변환만 하면 끝! (모범답안)
'''
def realSolution(n, left, right):
    answer = []
    # mtx에서 row, col위치가 큰 값이 value가 됨
    for i in range(left, right + 1): # 문제 해당부분만 배열 생성
        row = i // n  #  n값이 지나야 구분되니 몫 개념 사용
        col = i % n # n값으로 나눈 나머지가 패턴의 순서를 짚음
        max_val = max(row, col) # 큰 값이 value인 규칙 적용
        answer.append(max_val + 1) # 0부터 index 시작하였으므로 +1 후가

    return answer