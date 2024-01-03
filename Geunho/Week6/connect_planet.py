# https://www.acmicpc.net/problem/16398
# 전형적인 MST 문제, 모든 행성을 연결하고 그 유지비용을 최소화한다는 것에서 캐치하고 구현하면 됨
import sys

num_of_planets = int(sys.stdin.readline())
disjoint_set = [int(x) for x in range(num_of_planets + 1)]
rank = [0] * (num_of_planets + 1)


def find(planet: int) -> int:
    if disjoint_set[planet] != planet:
        disjoint_set[planet] = find(disjoint_set[planet])

    return disjoint_set[planet]


def union(planet1: int, planet2: int) -> None:
    root1 = find(planet1)
    root2 = find(planet2)

    if rank[root1] < rank[root2]:
        disjoint_set[root1] = root2
    elif rank[root1] > rank[root2]:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root2] = root1
        rank[root1] += 1


edges = []
for i in range(num_of_planets):
    costs = [int(x) for x in sys.stdin.readline().split()]

    for j in range(i + 1, num_of_planets):
        edges.append((i + 1, j + 1, costs[j]))


num_of_edges = 0
answer = 0
for edge_info in sorted(edges, key=lambda e: e[2]):
    p1, p2, cost = edge_info

    if find(p1) != find(p2):
        union(p1, p2)
        num_of_edges += 1
        answer += cost

    if num_of_edges == num_of_planets - 1:
        break

print(answer)
