# https://www.acmicpc.net/problem/1753
import heapq
import math
import sys
from collections import defaultdict

num_of_nodes, num_of_edges = [int(x) for x in sys.stdin.readline().split()]
start_node = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(num_of_edges):
    u, v, w = [int(x) for x in sys.stdin.readline().split()]
    graph[u].append((v, w))

INF = math.inf
distance_by_node = {n: INF for n in range(1, num_of_nodes + 1)}
distance_by_node[start_node] = 0

queue = []
heapq.heappush(queue, (distance_by_node[start_node], start_node))
while queue:
    current_distance, current_node = heapq.heappop(queue)

    if distance_by_node[current_node] < current_distance:
        continue

    for next_node, next_distance in graph[current_node]:
        candidate_distance = current_distance + next_distance
        if candidate_distance < distance_by_node[next_node]:
            distance_by_node[next_node] = candidate_distance
            heapq.heappush(queue, (candidate_distance, next_node))

answer = []
for node in range(1, num_of_nodes + 1):
    distance = distance_by_node[node]
    if distance == INF:
        answer.append("INF")
    else:
        answer.append(str(distance))

print("\n".join(answer))
