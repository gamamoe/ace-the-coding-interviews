# 목적: 미로탈출 최단시간   조건: 1칸 = 1초 = 거리, 레버 당기고 탈출구 가야함, 불가능 = -1
from collections import deque

# visited에서 거리까지 갱신하는 풀이
def bfs1(begin, finish, maps):  # (시작점, 끝점, 밑바탕 그래프)
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]  # 방문 통
    q = deque([begin])   # 시작점 대입 (리스트로해야 오류 안생김)

    while q:
        x, y = q.popleft()

        if x == finish[0] and y == finish[1]:  # 도착하면 종료
            return visited[finish[0]][finish[1]]  # 거리값 출력

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


## t(time)을 설정하는 풀이
def bfs2(begin, finish, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]  # 방문 통
    begin.append(0)  # time 초기값 t = 0을 삽입
    q = deque([begin])  # 시작점 대입

    while q:
        x, y, t = q.popleft()

        if x == finish[0] and y == finish[1]:
            return t

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append([nx, ny, t+1])  # t 갱신은 q내부에서해야 안전하다.


def solution(maps):
    for i in range(len(maps)):  # 행
        for j in range(len(maps[0])):  # 열
            if maps[i][j] == "S": start = [i, j]
            elif maps[i][j] == "L": lever = [i, j]
            elif maps[i][j] == "E": end = [i, j]

    distance1 = bfs2(start, lever, maps)
    distance2 = bfs2(lever, end, maps)

    return distance1 + distance2 if distance1 and distance2 else -1