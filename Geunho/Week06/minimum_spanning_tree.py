# https://www.acmicpc.net/problem/1197
import sys

V, E = [int(x) for x in sys.stdin.readline().split()]
disjoint_set = [x for x in range(V + 1)]
rank = [0] * (V + 1)


def find(vertex: int) -> int:
    if vertex != disjoint_set[vertex]:
        disjoint_set[vertex] = find(disjoint_set[vertex])

    return disjoint_set[vertex]


def union(vertex1: int, vertex2: int) -> None:
    root1 = find(vertex1)
    root2 = find(vertex2)

    if rank[root1] < rank[root2]:
        disjoint_set[root1] = root2
    elif rank[root1] > rank[root2]:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root2] = root1
        rank[root1] += 1


answer = 0
num_of_edges = 0
edges = []
for _ in range(E):
    v1, v2, cost = [int(x) for x in sys.stdin.readline().split()]
    edges.append((v1, v2, cost))

for data in sorted(edges, key=lambda e: e[2]):
    v1, v2, cost = data
    if num_of_edges == V - 1:
        break

    if find(v1) != find(v2):
        union(v1, v2)
        answer += cost
        num_of_edges += 1

print(answer)
