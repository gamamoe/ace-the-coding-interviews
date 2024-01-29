# https://www.acmicpc.net/problem/1260
import sys
from collections import defaultdict, deque

num_of_nodes, num_of_edges, start_node = [int(x) for x in sys.stdin.readline().split()]

graph = defaultdict(list)
for _ in range(num_of_edges):
    u, v = [int(x) for x in sys.stdin.readline().split()]
    graph[u].append(v)
    graph[v].append(u)


def dfs():
    stack = [start_node]
    visited = set()
    answer = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            answer.append(str(current_node))

            for next_node in sorted(graph[current_node], reverse=True):
                stack.append(next_node)

    return " ".join(answer)


def bfs():
    queue = deque([start_node])
    visited = {start_node}
    answer = []
    while queue:
        current_node = queue.popleft()
        answer.append(str(current_node))

        for next_node in sorted(graph[current_node]):
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

    return " ".join(answer)


print(f"{dfs()}\n{bfs()}")
