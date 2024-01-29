# https://www.acmicpc.net/problem/1647
# 문제 설명에서 MST의 느낌은 충분히 캐치할 수 있고, 마지막으로 `2개`의 마을로 분리한다는 아이디어만 떠올리면 됨
# MST를 만들고 가장 가중치가 높은 Edge만 하나 제거하면 자연스럽게 2개의 마을로 분리하게 된다
import sys

num_of_houses, num_of_roads = [int(x) for x in sys.stdin.readline().split()]
disjoint_set = [x for x in range(num_of_houses + 1)]
rank = [0] * (num_of_houses + 1)


def find(house: int) -> int:
    if disjoint_set[house] != house:
        disjoint_set[house] = find(disjoint_set[house])

    return disjoint_set[house]


def union(h1: int, h2: int) -> None:
    root1 = find(h1)
    root2 = find(h2)

    if rank[root1] < rank[root2]:
        disjoint_set[root1] = root2
    elif rank[root1] > rank[root2]:
        disjoint_set[root2] = root1
    else:
        disjoint_set[root2] = root1
        rank[root1] += 1


edges = []
for _ in range(num_of_roads):
    house1, house2, cost = [int(x) for x in sys.stdin.readline().split()]
    edges.append((house1, house2, cost))


num_of_edges = 0
answer = 0
for edge_info in sorted(edges, key=lambda e: e[2]):
    house1, house2, cost = edge_info

    if find(house1) != find(house2):
        union(house1, house2)
        num_of_edges += 1
        answer += cost

    if num_of_edges == num_of_houses - 1:
        answer -= cost
        break

print(answer)
