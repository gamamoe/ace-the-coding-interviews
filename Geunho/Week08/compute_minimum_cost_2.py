import heapq
import math
import sys
from collections import defaultdict, deque

num_of_cities = int(sys.stdin.readline())
num_of_buses = int(sys.stdin.readline())

graph = defaultdict(list)
distance_by_node = {}
previous_by_node = {}
for _ in range(num_of_buses):
    u, v, w = [int(x) for x in sys.stdin.readline().split()]
    graph[u].append((v, w))
    distance_by_node[u] = math.inf
    distance_by_node[v] = math.inf
    previous_by_node[u] = None
    previous_by_node[v] = None

start_node, end_node = [int(x) for x in sys.stdin.readline().split()]
queue = []
distance_by_node[start_node] = 0
heapq.heappush(queue, (distance_by_node[start_node], start_node))
while queue:
    current_distance, current_node = heapq.heappop(queue)

    if distance_by_node[current_node] < current_distance:
        continue

    for adjacent_node, adjacent_distance in graph[current_node]:
        candidate_distance = current_distance + adjacent_distance

        if candidate_distance < distance_by_node[adjacent_node]:
            distance_by_node[adjacent_node] = candidate_distance
            previous_by_node[adjacent_node] = current_node
            heapq.heappush(queue, (candidate_distance, adjacent_node))

node = end_node
path = deque([])
while node:
    path.appendleft(node)
    node = previous_by_node[node]

answer = [
    str(distance_by_node[end_node]),
    str(len(path)),
    " ".join([str(x) for x in path]),
]
print("\n".join(answer))
