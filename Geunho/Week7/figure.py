# https://www.acmicpc.net/problem/1926
import sys
from collections import deque
from typing import Tuple

n, m = [int(x) for x in sys.stdin.readline().split()]
graph = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().split()]
    graph.append(row)

visited = [[False] * m for _ in range(n)]


def bfs(start: Tuple[int, int]) -> int:
    def is_valid(coord: Tuple[int, int]) -> bool:
        return (
            0 <= coord[0] < n
            and 0 <= coord[1] < m
            and graph[coord[0]][coord[1]]
            and not visited[coord[0]][coord[1]]
        )

    queue = deque([start])
    visited[start[0]][start[1]] = True
    valid_nodes = [start]
    while queue:
        node = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_node = (node[0] + dx, node[1] + dy)

            if is_valid(next_node):
                valid_nodes.append(next_node)
                queue.append(next_node)
                visited[next_node[0]][next_node[1]] = True

    return len(valid_nodes)


num_of_figures = 0
maximum_margin = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            num_of_figures += 1
            current_margin = bfs((i, j))
            maximum_margin = max(maximum_margin, current_margin)


print(f"{num_of_figures}\n{maximum_margin}")
