### 트리

#### 트리 개념

트리는 앞에서 다룬 선형 자료구조와는 다르게 계층 구조를 표현하는 용도로 많이 사용하는 자료 구조  

- 인공지능의 의사결정트리
- Trie를 활용한 자동 완성이나 검색 기능
- 데이터베이스에서 데이터 삽입, 삭제, 검색을 빠르게 하기 위한 용도 (B-tree 계열)

여러 가지 새로운 용어들이 많이 등장하는 데 아래와 같다

- 루트 노드
- 노드/간선
- 형제 노드: 동일한 부모 노드를 갖는 노드
- 부모/자식 노드
- 리프 노드: 자식이 없는 노드
- 높이: 루트 노드를 레벨 0으로 보고 자식 노드로 내려가면서 1씩 증가
- 차수: 아래로 향하는 간선의 개수

#### 이진 트리 표현하기

이진 트리를 표현하는 방식은 크게 두 가지가 있다

1. 배열로 표현
2. 포인터로 표현

문제에서 메모리 사용량에 대한 부담이 없다면 구현이 쉬운 배열로 표현하고 접근하는 것이 빠르게 풀 가능성이 있음  
루트 노드를 1번으로 본다면 왼쪽 자식과 오른쪽 자식의 인덱스는 간단하게 k * 2, k * 2 + 1로 접근할 수 있다  
포인터 표현은 배열 표현에 비해 메모리 사용에 있어서 이득이 있지만 구현 난이도는 조금 있는 편

#### 이진 트리 순회하기

트리 순회 방식에는 전위순회, 중위순회, 후위순회 세 가지 방식이 있고 각각의 특징은 다음과 같다

- 전위 순회: 부모 -> 왼쪽 노드 -> 오른쪽 노드 순으로 순회하고 거치는 노드를 바로 방문하므로 직관적임. 트리를 복사할 때 많이 사용
- 중위 순회: 왼쪽 노드 -> 부모 -> 오른쪽 노드 순으로 순회하고, 이진탐색트리라면 정렬된 순서대로 값을 가져올 수 있게 됨
- 후위 순회: 왼쪽 노드 -> 오른쪽 노드 -> 부모 순으로 순회하고, 자식 노드부터 방문하므로 트리 삭제 시 유리함

#### 이진 탐색 트리

트리를 구성하는 것과 검색하는 방식을 이해해야 함  
트리를 구성할 때는 루트부터 시작하여 노드 값이 현재 노드보다 작으면 왼쪽에, 크다면 오른쪽에 반복적으로 거슬러 가면서 노드를 붙임  
검색할 때도 마찬가지로 찾고자 하는 값이 현재 노드와 같으면 검색이 종료되며, 만약 작다면 왼쪽으로 크다면 오른쪽으로 이동하면서 반복  
매번 탐색 시 루트의 반대쪽은 선택지에서 없어지므로 1/2씩 선택지가 없어짐, 따라서 시간복잡도는 O(logN) 시간복잡도를 가진다  
다만 한쪽으로 길게 몰린 트리는 결국 배열과 같으므로 O(N)이 되며, 이런 것을 방지하기 위한 고급 자료구조들이 존재한다 (AVL-tree, RB-tree) 등

### 문제 풀이

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

이 문제는 전체적인 형태가 트리인 것을 파악하는 것과 수익을 부모 노드에 전파하는 것을 어떻게 구현할지가 핵심인 문제  
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

최소 경로 (시간)을 요구하고 간선 웨이트가 없는 그래프이므로 BFS로 접근해야 한다  
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

#### [길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892)

앞에서 이론으로 배운 내용들을 조합해서 풀이하는 문제  

1. 우선 주어진 입력값으로 이진검색트리를 생성
2. 이진검색트리의 preorder와 postorder 구현

트리나 그래프 문제는 템플릿이 주어지지 않는다고 가정하고, 그냥 바로바로 구현할 수 있을 정도로 숙달되어야 한다고 본다

```python
from typing import List, Tuple


class TreeNode:
    def __init__(self, index, value, left=None, right=None):
        self.index = index
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, node: TreeNode = None):
        self.root = node

    def insert(self, node_info: Tuple[int, List[int]]):
        node_index = node_info[0]
        node_value = node_info[1][0]

        if not self.root:
            self.root = TreeNode(node_index, node_value)
            return

        current = self.root
        while current:
            if node_value < current.value:
                if current.left:
                    current = current.left
                    continue
                else:
                    current.left = TreeNode(node_index, node_value)
                    break
            else:
                if current.right:
                    current = current.right
                    continue
                else:
                    current.right = TreeNode(node_index, node_value)
                    break

    def get_pre_order(self) -> List[int]:
        stack = [self.root]
        path = []
        while stack:
            node = stack.pop()
            if node:
                path.append(node.index)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return path

    def get_post_order(self) -> List[int]:
        stack = [self.root]
        path = []
        visited = set()
        while stack:
            node = stack.pop()
            if node and node.index in visited:
                path.append(node.index)

            if node and node.index not in visited:
                stack.append(node)
            if node.right and node.right.index not in visited:
                stack.append(node.right)
            if node.left and node.left.index not in visited:
                stack.append(node.left)

            visited.add(node.index)

        return path


def solution(nodeinfo: List[List[int]]) -> List[List[int]]:
    node_index = [x + 1 for x in range(len(nodeinfo))]
    index_with_node_info = zip(node_index, nodeinfo)
    sorted_node_info = sorted(index_with_node_info, key=lambda p: p[1][1], reverse=True)

    tree = BST()
    for x in sorted_node_info:
        tree.insert(x)

    return [tree.get_pre_order(), tree.get_post_order()]


assert solution(
    [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
) == [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
```

preorder와 postorder 구현은 좀 더 neat한 코드들이 많았는 데 아래와 같다  
아주 직관적인 방식이라고 생각함. 그러나 스택을 이용한 iterative한 방식도 기억은 해두자

```python
def preorder(node):
    """
    1. 비어 있을 경우 [] return
    2. 자기자신을 먼저 방문후 left, right 순으로 방문 [root[0]] + preorder(left) + preorder(right)
    """
    if node is None:
        return []
    return [node.root[0]] + preorder(node.left) + preorder(node.right)


def postorder(data):
    """
    1. 비어 있을 경우 [] return
    2. left를 먼저 방문, right 방문 그 후 자기자신 방문 순으로 반환 postorder(left) + postorder(right) + [root[0]]
    """
    if data is None:
        return []
    return postorder(data.left) + postorder(data.right) + [data.root[0]]
```
