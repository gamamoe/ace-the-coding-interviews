### 실전 문제

#### [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

간선 가중치가 없는 케이스에서의 최단거리를 구해야하므로 아이디어로 BFS를 떠올리면 된다.  
몇 가지 예외 처리 (좌표, 벽)과 방문 불가능한 케이스만 주의하면 전형적인 BFS 코드로 풀이 가능

```python
from collections import deque
from typing import List


def solution(maps: List[List[int]]) -> int:
    def is_valid_coordinate(x: int, y: int) -> bool:
        return 0 <= x < m and 0 <= y < n and maps[y][x]

    n, m = len(maps), len(maps[0])

    queue = deque([((0, 0), 0)])
    visited = {(0, 0)}
    answer = -1
    while queue:
        coordinate, num_of_blocks = queue.popleft()

        if coordinate[0] == n - 1 and coordinate[1] == m - 1:
            answer = num_of_blocks + 1
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = coordinate[1] + dx
            next_y = coordinate[0] + dy
            next_coordinate = (next_y, next_x)
            if is_valid_coordinate(next_x, next_y) and next_coordinate not in visited:
                queue.append((next_coordinate, num_of_blocks + 1))
                visited.add(next_coordinate)

    return answer
```

#### [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

처음에는 Union-Find로 접근해야하나 싶었는데, 서브 네트워크가 트리가 아닌 경우도 있을 수 있으므로 DFS로 풀이해야한다는 것 캐치  
임의의 노드 (0번이라고 가정)에서 DFS를 쭉 돌고, 방문 처리를 한 후 방문되지 않은 노드를 다시 또 DFS를 하고  
최종적으로는 모든 노드가 방문할 때까지 DFS를 한 횟수가 연결된 네트워크의 갯수가 된다

```python
from typing import List


def solution(n: int, computers: List[List[int]]) -> int:
    def dfs(start: int):
        stack = [start]
        while stack:
            node = stack.pop()
            visited.add(node)

            for index, is_connected in enumerate(computers[node]):
                if index == node:
                    continue

                if is_connected and index not in visited:
                    stack.append(index)

    visited = set()
    answer = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1

    return answer


assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
```

### [배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)

그래프 간선의 가중치가 있고, 시작 마을에서 다른 모든 마을의 간선 합을 구해야 하며, 가중치는 음수가 없다  
조건을 보고 다익스트라 알고리즘을 생각할 수 있어야한다. 

```python
import heapq
from collections import defaultdict
from typing import List

INF = 500_001


def solution(N: int, road: List[List[int]], K: int) -> int:
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    distance_by_village = {v: INF for v in range(1, N + 1)}
    distance_by_village[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        current_distance, current_village = heapq.heappop(queue)

        if distance_by_village[current_village] < current_distance:
            continue

        for next_village, next_distance in graph[current_village]:
            candidate_distance = current_distance + next_distance

            if candidate_distance < distance_by_village[next_village]:
                distance_by_village[next_village] = candidate_distance
                heapq.heappush(queue, (candidate_distance, next_village))

    return len([x for x in distance_by_village.values() if x <= K])


assert (
    solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
    == 4
)
assert (
    solution(
        6,
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
        4,
    )
    == 4
)
```

#### [전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)

Idea -> `2 <= n <= 100` 이므로 시간 제약 조건이 빡빡하지 않은 점을 캐치해야 함  
주어진 wires에서 하나씩 빼고 그래프 생성 후, dfs를 활용하여 분리된 노드 갯수 세면서 갱신하는 식으로 아래와 같이 구현  
좀 더 스마트한 방법으로는 wires의 [u, v]가 끊어졌다고 가정하면, 아래 코드처럼 무식하게 1부터 n + 1까지 dfs를 방문 노드 모두 마킹할 때 까지가 아니라  
dfs(u), dfs(v) 두 번 호출하는 식으로도 작성이 가능하다, 또는 dfs(u)만 계산 후 전체 노드 갯수에서 빼도 된다

```python
import math
from collections import defaultdict
from typing import List, Set


def solution(n: int, wires: List[List[int]]) -> int:
    def dfs(start_node: int) -> Set[int]:
        stack = [start_node]
        node_set = set()
        while stack:
            current_node = stack.pop()
            if current_node not in node_set:
                node_set.add(current_node)
                for next_node in graph[current_node]:
                    stack.append(next_node)

        return node_set

    graph = defaultdict(set)
    for u, v in wires:
        graph[u].add(v)
        graph[v].add(u)

    answer = math.inf
    for u, v in wires:
        # Remove u, v
        graph[u].remove(v)
        graph[v].remove(u)

        visited = set()
        network_sizes = []
        for node in range(1, n + 1):
            if node not in visited:
                dfs_result = dfs(node)
                visited.update(dfs_result)
                network_sizes.append(len(dfs_result))

        answer = min(answer, abs(network_sizes[0] - network_sizes[1]))

        # Restore u, v
        graph[u].add(v)
        graph[v].add(u)

    return answer


assert (
    solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]) == 3
)
assert solution(4, [[1, 2], [2, 3], [3, 4]]) == 0
assert solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1
```

### 추가 문제

#### [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)

간선 가중치가 없고, 특정 노드 (1번 노드)에서 가장 먼 노드의 갯수를 구하는 것이므로 BFS를 통해 쉽게 계산할 수 있다

```python
from collections import defaultdict, deque
from typing import List


def solution(n: int, edge: List[List[int]]) -> int:
    graph = defaultdict(list)

    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    start_node = 1
    queue = deque([(start_node, 0)])
    visited = {start_node: 1}
    max_distance = 1
    while queue:
        current_node, current_distance = queue.popleft()
        max_distance = max(max_distance, current_distance)

        for next_node in graph[current_node]:
            if next_node not in visited:
                visited[next_node] = current_distance + 1
                queue.append((next_node, current_distance + 1))

    answer = len(
        [node for node, distance in visited.items() if distance == max_distance]
    )
    return answer


assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3
```

#### [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)

간선 가중치가 있는 그래프이며, 음의 가중치는 없고 최소 (또는 최단) 관련 문제이므로 다익스트라 알고리즘으로 접근했다  
예제 3개를 통해서 얻을 수 있는 경우의 수는 다음과 같다

1. 시작점부터 경유지(경유지는 도착지와는 다른 노드)까지 동행 후, 경유지에서 각각의 도착지까지의 합이 최소 비용인 경우
2. 처음부터 시작점에서 각각의 도착지까지의 합이 최소 비용인 경우
3. 시작점부터 경유지를 거치지만, 경유지가 둘 중 하나의 도착지와 같은 경우

내 경우 다익스트라 알고리즘을 통해 우선 시작점 -> 도착지 A, 시작점 -> 도착지 B의 비용 합을 먼저 계산했다  
그 후 가능한 중간 노드를 순회하는데, 이 때 시작점 -> 경유지는 이전 과정에서의 distance를 활용해서 바로 게산할 수 있고  
시작점을 경유지로 하는 다익스트라 알고리즘을 다시 계산하여 경유지 -> 도작지 A, 경유지 -> 도착지 B를 계산함  
최종적으로는 가능한 케이스 중 최솟값을 반환하는 방식, 다익스트라 알고리즘 한번의 시간복잡도를 O(ElogV)로 본다면 해당 풀이는 O(V*ElogV)

```python
import heapq
import math
from collections import defaultdict
from typing import List, Dict


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    graph = defaultdict(list)

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def shortest_path(start_node: int) -> Dict[int, float]:
        distance_by_node = {node: math.inf for node in range(1, n + 1)}
        distance_by_node[start_node] = 0
        queue = []
        heapq.heappush(queue, (distance_by_node[start_node], start_node))

        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if distance_by_node[current_node] < current_distance:
                continue

            for adjacent_node, cost in graph[current_node]:
                alternative_distance = current_distance + cost
                if alternative_distance < distance_by_node[adjacent_node]:
                    distance_by_node[adjacent_node] = alternative_distance
                    heapq.heappush(queue, (alternative_distance, adjacent_node))

        return distance_by_node

    shortest_distance_from_start = shortest_path(s)
    answer = shortest_distance_from_start[a] + shortest_distance_from_start[b]
    for stopover_node in range(1, n + 1):
        shortest_distance_from_stopover = shortest_path(stopover_node)
        answer = min(
            answer,
            shortest_distance_from_start[stopover_node]
            + shortest_distance_from_stopover[a]
            + shortest_distance_from_stopover[b],
        )

    return answer


assert (
    solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
    == 82
)
assert (
    solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]) == 14
)
assert (
    solution(
        6,
        4,
        5,
        6,
        [
            [2, 6, 6],
            [6, 3, 7],
            [4, 6, 7],
            [6, 5, 11],
            [2, 5, 12],
            [5, 3, 20],
            [2, 4, 8],
            [4, 3, 9],
        ],
    )
    == 18
)
```
