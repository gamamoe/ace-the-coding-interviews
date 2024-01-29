import sys


N = int(sys.stdin.readline())

disjoint_set = [x for x in range(N + 1)]
rank = [0] * (N + 1)
edge_info_list = []

for i in range(N):
    w = int(sys.stdin.readline())
    edge_info_list.append((i, N, w))

for i in range(N):
    costs = [int(x) for x in sys.stdin.readline().split()]
    for j in range(i + 1, N):
        edge_info_list.append((i, j, costs[j]))


def find(v: int) -> int:
    if disjoint_set[v] != v:
        disjoint_set[v] = find(disjoint_set[v])

    return disjoint_set[v]


def union(v1: int, v2: int) -> None:
    root1 = find(v1)
    root2 = find(v2)

    if rank[root1] < rank[root2]:
        disjoint_set[root1] = root2
    elif rank[root1] > rank[root2]:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root2] = root1
        rank[root1] += 1


answer = 0
num_of_edges = 0
for edge_info in sorted(edge_info_list, key=lambda e: e[2]):
    if num_of_edges == N:
        break

    v1, v2, cost = edge_info
    root1 = find(v1)
    root2 = find(v2)

    if root1 != root2:
        union(v1, v2)
        answer += cost
        num_of_edges += 1

print(answer)
