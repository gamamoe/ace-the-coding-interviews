# https://www.acmicpc.net/problem/7576
# 익은 토마토 상, 하, 좌, 우의 익지 않은 토마토는 하루 후 익게 됨
# 모두 다 익게 되는 `최소` 일수, 따라서 BFS로 접근
import copy
import sys
from collections import deque
from typing import Set, Tuple

num_of_cols, num_of_rows = [int(x) for x in sys.stdin.readline().split()]
graph = []
start_nodes = set()
num_of_tomatoes = 0
for row in range(num_of_rows):
    current_row = [int(x) for x in sys.stdin.readline().split()]
    graph.append(current_row)

    for col in range(num_of_cols):
        if current_row[col] == 1:
            start_nodes.add((row, col))
            num_of_tomatoes += 1
        elif current_row[col] == 0:
            num_of_tomatoes += 1
        else:
            continue


queue = deque([(start_nodes, 0)])
visited = copy.deepcopy(start_nodes)


def is_valid(r: int, c: int, check: Set[Tuple[int, int]]) -> bool:
    return (
        0 <= r < num_of_rows
        and 0 <= c < num_of_cols
        and not graph[r][c]
        and (r, c) not in check
    )


answer = 0
while queue:
    nodes, days = queue.popleft()
    next_nodes = set()

    for row, col in nodes:
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row = row + drow
            next_col = col + dcol

            if is_valid(next_row, next_col, visited):
                next_node = (next_row, next_col)
                next_nodes.add(next_node)
                visited.add(next_node)

    if next_nodes:
        queue.append((next_nodes, days + 1))
    else:
        answer = days if num_of_tomatoes == len(visited) else -1
        break

print(answer)
