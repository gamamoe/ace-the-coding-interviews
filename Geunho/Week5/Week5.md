
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