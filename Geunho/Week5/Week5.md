
#### 트리 순회

```python
from typing import List


def pre_order(nodes: List[int], index: int) -> str:
    if index < len(nodes):
        result = f"{nodes[index]} "
        result += pre_order(nodes, index * 2 + 1)
        result += pre_order(nodes, index * 2 + 2)
        return result
    else:
        return ""


def in_order(nodes: List[int], index: int) -> str:
    if index < len(nodes):
        result = in_order(nodes, index * 2 + 1)
        result += f"{nodes[index]} "
        result += in_order(nodes, index * 2 + 2)
        return result
    else:
        return ""


def post_order(nodes: List[int], index: int) -> str:
    if index < len(nodes):
        result = post_order(nodes, index * 2 + 1)
        result += post_order(nodes, index * 2 + 2)
        result += f"{nodes[index]} "
        return result
    else:
        return ""


def solution(nodes: List[int]) -> List[str]:
    pre_order_result = pre_order(nodes, 0)
    in_order_result = in_order(nodes, 0)
    post_order_result = post_order(nodes, 0)

    return [
        pre_order_result.strip(),
        in_order_result.strip(),
        post_order_result.strip(),
    ]


assert solution([1, 2, 3, 4, 5, 6, 7]) == [
    "1 2 4 5 3 6 7",
    "4 2 5 1 6 3 7",
    "4 5 2 6 7 3 1",
]
```

#### 이진 탐색 트리 구현

```python
from typing import List


class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    def search(self, key: int) -> bool:
        curr = self.root

        while True:
            if not curr:
                break

            if key == curr.val:
                return True
            elif key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return False


def solution(lst: List[int], search_lst: List[int]) -> List[bool]:
    bst = BST()
    for element in lst:
        bst.insert(element)

    return [bst.search(x) for x in search_lst]


assert solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]) == [True, True, True, False]
assert solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [
    False,
    False,
    False,
    False,
    False,
]
```

#### [예상 대진표](https://school.programmers.co.kr/learn/courses/30/lessons/12985)

입출력 예제를 손으로 써가면서 접근하면 쉽게 풀 수 있다  
아이디어는 이진 트리를 배열로 표현할 때 같은 형제는 동일한 k를 가진다는 것에서 착안하면 된다  
예를 들어 1과 2는 각각 k가 0인 2 * k, 2 * k + 1이며 7과 8은 k가 3인 2 * k, 2 * k + 1이다  
같은 형제는 다음 라운드에서 항상 2로 나눈 몫으로 인덱스가 변경되므로, 그 인덱스가 동일하면 라운드에서 붙는 경우라고 볼 수 있다  
예를 들어, 5와 6은 인덱스가 각각 4와 5인데 이를 2로 나눈 몫은 모두 2이므로 1라운드에서 붙게 됨  
다른 예로, 4와 5는 인덱스가 각각 3과 4인데 3 -> 1 -> 0 -> 0, 4 -> 2 -> 1 -> 0 으로 갱신이 되고 3라운드에서 붙게 된다  

```python
def solution(n: int, a: int, b: int) -> int:
    a -= 1
    b -= 1
    answer = 0
    while a != b:
        a //= 2
        b //= 2
        answer += 1

    return answer


assert solution(8, 4, 7) == 3
assert solution(8, 4, 5) == 3
assert solution(8, 5, 6) == 1
```

#### [다단계 칫솔 판매](https://school.programmers.co.kr/learn/courses/30/lessons/77486)

이 문제는 전체적인 형태가 트리인 것을 파악하는 것과 수익을 부모 노드에게 전파하는 것을 어떻게 구현할 지가 핵심인 문제  
트리 구현을 책에서 배운 배열 표현이나 이진 트리의 형태로 생각하면 어렵게 풀 가능성이 생긴다  
필요한 것은 현재 노드, 그리고 그것의 부모 노드와 필요하다면 수익을 저장할 변수 정도이므로 간단하게  
현재 노드: (부모 노드, 현재 노드의 수익)과 같은 딕셔너리를 정의하면 쉽게 풀이할 수 있다  
아이디어는 현재 노드부터 루트 노드까지 계속 노드를 갱신하는 부분이며 `current_node = node_by_name[current_node.parent]`  
시간 초과를 해결하기 위해서는 특정 노드에서 수익이 0원이라면 상위 노드로 전파할 필요가 없으므로 적절히 break를 해줘야한다  
그 외 코드 간결을 위해서 자잘한 트릭들 (루트 노드의 Parent는 None 설정 등)도 추가함

```python
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    parent: Optional[str]
    value: int


def solution(
    enroll: List[str], referral: List[str], seller: List[str], amount: List[int]
) -> List[int]:
    node_by_name = {child: Node(parent, 0) for child, parent in zip(enroll, referral)}
    node_by_name["-"] = Node(None, 0)

    for name, sell_count in zip(seller, amount):
        interest = sell_count * 100
        current_node = node_by_name[name]

        while current_node.parent:
            if interest == 0:
                break

            parent_interest = int(interest * 0.1)
            current_node.value += interest - parent_interest
            interest = parent_interest
            current_node = node_by_name[current_node.parent]

    return [node_by_name[name].value for name in enroll]


assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10],
) == [360, 958, 108, 0, 450, 18, 180, 1080]

assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4],
) == [0, 110, 378, 180, 270, 450, 0, 0]
```

#### [미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993)

최소 경로 (시간)을 요구하고 간선 웨이트가 없는 그래프이므로 BFS로 접근을 해야한다  
트리는 그래프의 일종으로 볼 수 있기 때문에 주로 그래프에서 많이 보는 BFS 알고리즘을 활용한 문제는 좋으나 문제 배치가 조금 아쉬운 부분이 있음  
BFS의 의사 코드는 아래와 같다 ( https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode )

```
#  1  procedure BFS(G, root) is
#  2      let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)
```

레버를 반드시 당기고 탈출해야 하므로, BFS를 두 번 (Start -> Lever) 그리고 (Lever -> End)하는 방식으로 접근하였음  
위의 의사 코드를 구현하되, 경로 길이를 저장할 변수를 하나 고려해서 BFS마다 갱신하도록 한다  
책의 풀이는 visited를 확장하여 L을 마크한 시점에 다른 인덱스를 쓰는 방식으로 구현되어 있어서 BFS를 한 번만 해도 되는 풀이  
가독성은 BFS를 그냥 두 번 하는 것이 더 나은 것 같다

```python
from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    x: int
    y: int
    path_length: int


def bfs(maps: List[str], start_coordinate: Coordinate, end_marker: str) -> int:
    m, n = len(maps), len(maps[0])
    visited = [[False] * n for _ in range(m)]
    visited[start_coordinate.y][start_coordinate.x] = True
    queue = deque([start_coordinate])

    while queue:
        coordinate = queue.popleft()
        x, y, path_length = coordinate.x, coordinate.y, coordinate.path_length

        if maps[y][x] == end_marker:
            return path_length

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_y, new_x = y + dy, x + dx

            if not (0 <= new_y < m) or not (0 <= new_x < n):
                continue

            if maps[new_y][new_x] == "X":
                continue

            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                queue.append(Coordinate(x=new_x, y=new_y, path_length=path_length + 1))

    return -1


def solution(maps: List[str]) -> int:
    m, n = len(maps), len(maps[0])

    start_coordinate, lever_coordinate = None, None
    for y in range(m):
        for x in range(n):
            if maps[y][x] == "S":
                start_coordinate = Coordinate(x, y, 0)
            elif maps[y][x] == "L":
                lever_coordinate = Coordinate(x, y, 0)
            else:
                continue

    start_to_lever = bfs(maps, start_coordinate, "L")
    lever_to_end = bfs(maps, lever_coordinate, "E")

    if start_to_lever == -1 or lever_to_end == -1:
        return -1

    return start_to_lever + lever_to_end


assert solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]) == 16
assert solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]) == -1
```