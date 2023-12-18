
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
