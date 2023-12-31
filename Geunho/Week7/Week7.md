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