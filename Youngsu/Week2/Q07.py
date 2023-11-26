def solution(dirs):
    answer = 0
    # 딕셔너리 구조 사용? {(x,y):(u,d,r,l)}
    # 2차원 배열? [[-5,-5] ~ [5,5]] 11*11 = 121개
    # [0,0] ~ [10,10] : 좌표는 인덱스에서 5만큼 빼면 됨
    # 사실 시작을 [5,5]에서 한다고 가정하고 그냥 풀면 됨
    # 경계 : x == 0, 10 y == 0, 10에서 명령 들어올 때 처리
    # 3차원 배열로 하면 되는 거 아닌가? 딕셔너리 불필요? 아니면 2차원배열에 원소가 딕셔너리?
    # [[[0,0,0,0], [0,0,0,0], .... [0,0,0,0]] 같은 형식
    # 각 리스트는 [U,D,R,L] 횟수
    # 예를 들어 좌표 (5,5)에서 D 명령을 받으면,
    # matrix[5][5][1]이 0이면 1로 바꾸고, 1이면 그대로.
    
    # 3차원 배열 만들기
    matrix = [[[0 for _ in range(4)] for _ in range(11)] for _ in range(11)]

    # 시작 좌표
    x, y = 5, 5

    # 방향 리스트
    # dir = ["U", "D", "R", "L"]

    # 명령 처리하기
    for c in dirs:       
        if (c == "U") and (y != 10):
            if (matrix[x][y][0] == 0) and (matrix[x][y + 1][1] == 0):
                matrix[x][y][0] = 1
                answer += 1
            y += 1
        elif (c == "D") and (y != 0):
            if (matrix[x][y][1] == 0) and (matrix[x][y - 1][0] == 0):
                matrix[x][y][1] = 1
                answer += 1
            y -= 1
        elif (c == "R") and (x != 10):
            if (matrix[x][y][2] == 0) and (matrix[x + 1][y][3] == 0):
                matrix[x][y][2] = 1
                answer += 1
            x += 1
        elif (c == "L") and (x != 0):
            if (matrix[x][y][3] == 0) and (matrix[x - 1][y][2] == 0):
                matrix[x][y][3] = 1
                answer += 1
            x -= 1
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDLRDURL"))

