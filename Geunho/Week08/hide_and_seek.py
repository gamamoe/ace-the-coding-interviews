# https://www.acmicpc.net/problem/1697
# 다음 방문 가능 노드가 X-1, X+1, 2*X 세 가지 케이스인 BFS
import sys
from collections import deque

start, destination = [int(x) for x in sys.stdin.readline().split()]

queue = deque([(start, 0)])
visited = {start}

while queue:
    current, seconds = queue.popleft()

    if current == destination:
        print(seconds)
        break

    for next_candidate in [current - 1, current + 1, 2 * current]:
        if 0 <= next_candidate <= 100_000 and next_candidate not in visited:
            queue.append((next_candidate, seconds + 1))
            visited.add(next_candidate)
