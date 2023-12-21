# 목적: 미로탈출 최단시간   조건: 1칸 = 1초 = 거리, 레버 당기고 탈출구 가야함, 불가능 = -1
from collections import deque

def bfs(begin, finish, maps):  # (시작점, 끝점, 밑바탕 그래프)
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]  # 방문 통
    q = deque()
    q.append(begin)  # 시작점 대입

    while q:
        x, y = q.popleft()

        if x == finish[0] and y == finish[1]:  # 도착하면 종료
            return visited[finish[0]][finish[1]]  # 거리값 출력

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))



## 이건 왜 안되는지 모르겠는 코드..
def whybfs(begin, finish, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]  # 방문 통
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 좌표
    q = deque()
    q.append(begin)  # 시작점 대입
    t = 0  # 시간
    while q:
        x, y = q.popleft()

        if x == finish[0] and y == finish[1]:
            return t

        for i in range(4):  # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                t += 1
                visited[nx][ny] = True
                q.append((nx, ny))


def solution(maps):
    for i in range(len(maps)):  # 행
        for j in range(len(maps[0])):  # 열
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)

    distance1 = bfs(start, lever, maps)
    distance2 = bfs(lever, end, maps)

    return distance1 + distance2 if distance1 and distance2 else -1