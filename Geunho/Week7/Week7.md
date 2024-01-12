### 그래프의 개념

노드와 간선을 이용한 비선형 자료 구조. 간선은 1) 무방향/유방향 2) 가중치 O/X 조합이 가능함
방향이 있는 그래프를 Directed Graph, 없는 그래프를 Undirected Graph 라고 한다
특정 노드에서 시작해 다시 돌아오는 경로가 있을 경우 Cycle (순혼)이 존재한다고 하며 Cycle Graph라고 함

### 그래프 구현

- 인접 행렬
- 인접 리스트

인접 행렬 구현은 배열을 주로 활용하며, 배열의 인덱스는 노드 그리고 값은 노드의 가중치로 볼 수 있다
반대로 인접 리스트 구현은 배열과 노드 객체를 이용해서 주로 표현함. 그러면 배열의 인덱스는 시작 노드를 의미하며 값에는 다음 노드를 연결할 수 있음

인접 행렬은 노드 수에 비해 간선 수가 적은 희소 그래프를 표현할 때 많은 공간이 낭비되는 단점이 있고, 노드 인덱스의 값의 차이가 크게 나도 비슷하게 공간 낭비 문제가 생김

인접 리스트는 구현이 상대적으로 어렵지만 낭비되는 공간 없이 실제 연결된 노드에 대해서만 연결하면 되는 장점이 있다. 다만 간선 정보를 확인할 때는 특정 노드에서 시작하여 연결된 리스트를 모두 순회하면서 확인해야 함

보통은 시간 제약에서 장점을 취하기 위해 인접 행렬 방식으로 푸는 경우가 많고, 노드 개수가 1000개 미만이라면 인접 행렬을 사용해도 큰 무리가 없을 가능성이 높음

### 그래프 탐색

- 깊이 우선 탐색: 더 이상 탐색할 노드가 없을 때까지 진행하다가, 최근 방문했던 노드로 돌아간 후 다시 다음 가지 않은 노드 방문
- 너비 우선 탐색: 현재 위치에서 가장 가까운 노드부터 모두 방문하고, 다음 노드로 넘어감. 그 노드에서 다시 또 가장 가까운 노드부터 모드 방문

  깊이 우선 탐색은 재귀 호출 또는 스택을 사용해서 구현 가능하며, 너비 우선 탐색은 큐를 활용하여 구현함
  깊이 우선 탐색은 깊에 탐색 후 되돌아오는 특성이 있고, 따라서 모든 가능한 해를 찾는 알고리즘 구현이나 그래프 사이클 감지에 활용
  너비 우선 탐색은 가중치가 없는 그래프에서의 최단 경로를 보장, 최단 경로나 네트워크 분석 문제 풀 때 활용

### 다익스트라 알고리즘

그래프 형태에 따라 다르지만, 최단 경로의 뉘앙스가 나는 문제는 대부분 다익스트라 알고리즘으로 접근 가능  
예외) 간선의 가중치가 없거나 (이 경우 BFS 접근), 음수 가중치가 있는 경우 (벨만-포드 알고리즘)  

의사 코드는 다음과 같다
1. 거리와 직전 노드를 저장할 자료구조를 선언하고, 방문하지 않은 노드 중 가장 비용이 작은 노드를 선택
2. 현재 노드에서 이동 가능한 노드의 거리와 최소 비용의 합이 기존 노드 거리보다 작으면 갱신
3. 이 과정을 계속 반복한다

```shell
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
```

최단 거리는 prev를 거슬러 올라가면서 구하면 되는 데, 의사 코드는 아래와 같음

```shell
1  S ← empty sequence
2  u ← target
3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
4      while u is defined:                       // Construct the shortest path with a stack S
5          insert u at the beginning of S        // Push the vertex onto the stack
6          u ← prev[u]                           // Traverse from target to source
```

우선순위 큐를 활용하면 더 효율적으로 계산이 가능하며 의사코드는 아래와 같다
```shell
1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex priority queue Q
5
6      for each vertex v in Graph.Vertices:
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9              prev[v] ← UNDEFINED                // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // Go through all v neighbors of u
17             alt ← dist[u] + Graph.Edges(u, v)
18             if alt < dist[v]:
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev
```

파이썬에서는 decrase_priority가 없으므로 Q 초기화 시 시작 노드만 넣고, decrease priority를 heap push로 변경하는 식으로도 구현이 가능하다
> Instead of filling the priority queue with all nodes in the initialization phase, it is also possible to initialize it to contain only source; then, inside the if alt < dist[v] block, the decrease_priority() becomes an add_with_priority() operation if the node is not already in the queue.[7]: 198 

### 벨만 포드 알고리즘

다익스트라 알고리즘과 마찬가지로 노드에서 노드까지의 최소 비용을 구하는 알고리즘  
다익스트라 알고리즘과 다르게 음의 가중치가 있어도 최단 경로를 구할 수 있고, 음의 순환 역시 감지할 수 있다

```shell
function BellmanFord(list vertices, list edges, vertex source) is

    // This implementation takes in a graph, represented as
    // lists of vertices (represented as integers [0..n-1]) and edges,
    // and fills two arrays (distance and predecessor) holding
    // the shortest path from the source to each vertex

    distance := list of size n
    predecessor := list of size n

    // Step 1: initialize graph
    for each vertex v in vertices do
        // Initialize the distance to all vertices to infinity
        distance[v] := inf
        // And having a null predecessor
        predecessor[v] := null
    
    // The distance from the source to itself is, of course, zero
    distance[source] := 0

    // Step 2: relax edges repeatedly
    repeat |V|−1 times:
        for each edge (u, v) with weight w in edges do
            if distance[u] + w < distance[v] then
                distance[v] := distance[u] + w
                predecessor[v] := u

    // Step 3: check for negative-weight cycles
    for each edge (u, v) with weight w in edges do
        if distance[u] + w < distance[v] then
            predecessor[v] := u
            // A negative cycle exists; find a vertex on the cycle 
            visited := list of size n initialized with false
            visited[v] := true
            while not visited[u] do
                visited[u] := true
                u := predecessor[u]
            // u is a vertex in a negative cycle, find the cycle itself
            ncycle := [u]
            v := predecessor[u]
            while v != u do
                ncycle := concatenate([v], ncycle)
                v := predecessor[v]
            error "Graph contains a negative-weight cycle", ncycle
    return distance, predecessor
```

### 몸풀기 문제

#### 깊이 우선 탐색 순회

스택를 활용한 DFS 구현

```bash
procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
```

```python
from collections import defaultdict
from typing import List


def solution(graph: List[List[str]], start: str) -> List[str]:
    adjacent_list = defaultdict(list)

    for from_node, to_node in graph:
        adjacent_list[from_node].append(to_node)

    visited = set()
    stack = [start]
    answer = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            answer.append(node)

            for next_node in adjacent_list[node][::-1]:
                stack.append(next_node)

    return answer
```

재귀로 구현한 DFS

```bash
procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

```python
from collections import defaultdict
from typing import List


def solution(graph: List[List[str]], start: str) -> List[str]:
    adjacent_list = defaultdict(list)

    for from_node, to_node in graph:
        adjacent_list[from_node].append(to_node)

    visited = set()
    answer = []

    def dfs(current_node: str):
        visited.add(current_node)
        answer.append(current_node)

        for node in adjacent_list[current_node]:
            if node not in visited:
                dfs(node)

    dfs(start)
    return answer


assert solution([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "A") == [
    "A",
    "B",
    "C",
    "D",
    "E",
]
assert solution(
    [["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]], "A"
) == ["A", "B", "D", "E", "F", "C"]
```

#### 너비 우선 탐색 순회

큐를 이용하여 쉽게 구현할 수 있음, DFS의 iterative 구조와 거의 유사

```bash
 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
```

```python
from collections import defaultdict, deque
from typing import List, Tuple


def solution(graph: List[Tuple[int, int]], start: int) -> List[int]:
    adjacent_list = defaultdict(list)

    for u, v in graph:
        adjacent_list[u].append(v)

    queue = deque([start])
    visited = {start}
    answer = []
    while queue:
        node = queue.popleft()
        answer.append(node)
        queue.extend([x for x in adjacent_list[node] if x not in visited])
        visited.update(adjacent_list[node])

    return answer


assert solution(
    [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1
) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1) == [
    1,
    2,
    3,
    4,
    5,
    0,
]
```

#### 다익스트라 알고리즘

저자 코드와는 약간 상이하지만 전체적인 맥락은 동일함, 큐에서 빼고 경로를 갱신한다는 아이디어를 잘 가져갈 것

```python
import heapq
import sys
from collections import deque
from typing import Dict, List


def solution(graph: Dict[str, Dict[str, int]], start: str) -> List:
    queue = [(0, start)]
    check = {start}

    dist = {node: sys.maxsize for node in graph}
    dist[start] = 0
    prev = {start: start}

    while queue:
        dist_u, u = heapq.heappop(queue)
        for v, edge_dist in graph[u].items():
            alt = dist_u + edge_dist
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                if v not in check:
                    check.add(v)
                    heapq.heappush(queue, (alt, v))

    def get_path(target):
        path = deque()
        current_node = target

        while current_node != start:
            path.appendleft(current_node)
            current_node = prev[current_node]

        path.appendleft(start)
        return list(path)

    path_result = {v: get_path(v) for v in graph}
    return [dist, path_result]


assert solution({"A": {"B": 9, "C": 3}, "B": {"A": 5}, "C": {"B": 1}}, "A") == [
    {"A": 0, "B": 4, "C": 3},
    {"A": ["A"], "B": ["A", "C", "B"], "C": ["A", "C"]},
]
assert solution({"A": {"B": 1}, "B": {"C": 5}, "C": {"D": 1}, "D": {}}, "A") == [
    {"A": 0, "B": 1, "C": 6, "D": 7},
    {"A": ["A"], "B": ["A", "B"], "C": ["A", "B", "C"], "D": ["A", "B", "C", "D"]},
]
```

#### 벨만-포드 알고리즘

```python
import math
from typing import List, Tuple, Any, Union, Dict, Optional


def solution(
    graph: List[List[Tuple[int, int]]], source: int
) -> List[Union[List[Any], int]]:
    def relax_edges() -> bool:
        has_cycle = False
        for current_node in range(num_of_nodes):
            for next_node, next_dist in adjacent_list[current_node]:
                if dist_by_node[current_node] + next_dist < dist_by_node[next_node]:
                    dist_by_node[next_node] = dist_by_node[current_node] + next_dist
                    predecessor_by_node[next_node] = current_node
                    has_cycle = True

        return has_cycle

    adjacent_list = {}
    dist_by_node = {}
    predecessor_by_node: Dict[int, Optional[int]] = {}
    num_of_nodes = len(graph)
    for node, connection in enumerate(graph):
        adjacent_list[node] = connection
        dist_by_node[node] = math.inf
        predecessor_by_node[node] = None

    dist_by_node[source] = 0
    for _ in range(num_of_nodes - 1):
        relax_edges()

    has_negative_cycle = relax_edges()
    if has_negative_cycle:
        answer = [-1]
    else:
        result_distance = [dist_by_node[x] for x in range(num_of_nodes)]
        result_predecessor = [predecessor_by_node[x] for x in range(num_of_nodes)]
        answer = [result_distance, result_predecessor]

    return answer


assert solution(
    [[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0
) == [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
assert solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0) == [-1]
```

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

### 추가 문제

### 가장 먼 노드

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
