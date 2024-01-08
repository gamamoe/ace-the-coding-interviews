### 집합과 상호배타적 집합의 개념

집합은 순서와 중복이 없는 원소들을 갖는 자료구조, Python에서는 간단하게 `set()`을 활용할 수 있다. 
상호배타적 집합은 서로 다른 두 집합 사이에 공통 원소가 없는 경우를 말함

코딩 테스트에서 상호배타적 집합을 활용하는 가장 큰 이유는 그래프 알고리즘 중 **사이클**을 판별하기 위해서 활용.
그 외에는 아래와 같은 응용 사례들이 존재한다

- 이미지 분할
- 도로 네트워크 구성
- 최소 신장 트리 알고리즘 구현
- 게임 개발
- 클러스터링 작업

### 집합의 연산

집합의 표현은 앞서 배운 트리의 배열 표현과 거의 유사하게 구현할 수 있고, 대표적인 연산은 합치기와 탐색 (Union-Find)가 있음. 
배열의 인덱스는 자기 자신, 그리고 그 인덱스에 해당 하는 값은 부모 노드를 의미하고 만약 인덱스와 인덱스에 해당하는 부모 노드 값이 같다면 
그것은 루트 노드를 의미한다. 보통 초기화 시 부모 노드는 자기 자신으로 설정하고 알고리즘이 진행되면서 채워지게 됨

```python
# 인덱스와 인덱스에 해당하는 값이 같은 값을 가지도록 초기화
num_of_nodes = 5
disjoint_set = [x for x in range(num_of_nodes)]
```

### 유니온-파인드 알고리즘

파인드 연산은 특정 노드의 루트 노드가 무엇인지 탐색하는 방법이고, 만약 두 노드의 파인드 연산 결과가 같다면 동일한 루트 노드를 가진다는 의미로 볼 수 있다. 
즉, 반대로 생각하면 사이클이 형성되는 지 여부도 파인드 연산의 결과 비교를 통해서 가능함

```python
disjoint_set = [x for x in range(num_of_nodes)]
def find(node: int) -> int:
    if disjoint_set[node] != node:
        # 아래 호출을 통해서 경로 압축이 발생
        disjoint_set[node] = find(disjoint_set[node])
    return disjoint_set[node]
```

합치기 연산은 두 집합을 하나로 합치는 연산이고, 다시 말하면 두 집합의 루트 노드를 같게 하는 것. 
루트 노드는 두 집합의 루트 노드 중 하나가 되면 되지만, 보통 rank 개념을 도입해서 처리를 한다. 
아이디어는 rank가 낮은 집합의 루트 노드의 부모 노드를 rank가 큰 집합의 루트 노드로 변경. 
만약 rank가 같다면 둘 중 하나를 root 노드로 갱신하고 rank 값도 1 증가

```python
disjoint_set = [x for x in range(num_of_nodes)]
rank = [0] * num_of_nodes
def union(node1: int, node2: int) -> None:
    root_of_node1 = find(node1)
    root_of_node2 = find(node2)

    if rank[root_of_node1] < rank[root_of_node2]:
        disjoint_set[root_of_node1] = root_of_node2
    elif rank[root_of_node1] > rank[root_of_node2]:
        disjoint_set[root_of_node2] = root_of_node1
    else:
        disjoint_set[root_of_node2] = root_of_node1
        rank[root_of_node1] += 1
```

### 몸풀기 문제

#### 간단한 유니온-파인드 알고리즘 구현하기

```python
from typing import List, Union


def solution(k: int, operations: List[List[Union[int, str]]]) -> int:
    disjoint_set = [x for x in range(k)]

    def _union(node_index1: int, node_index2: int) -> None:
        root_index1 = _find(node_index1)
        root_index2 = _find(node_index2)

        if root_index1 < root_index2:
            disjoint_set[node_index2] = root_index1
        else:
            disjoint_set[node_index1] = root_index2

    def _find(node_index: int) -> int:
        if node_index == disjoint_set[node_index]:
            return node_index

        return _find(disjoint_set[node_index])

    for operation in operations:
        if operation[0] == "u":
            _union(operation[1], operation[2])
        else:
            _find(operation[1])

    answer = 0
    for index, value in enumerate(disjoint_set):
        if index == value:
            answer += 1
    return answer


assert solution(3, [["u", 0, 1], ["u", 1, 2], ["f", 2]]) == 1
assert solution(4, [["u", 0, 1], ["u", 2, 3], ["f", 0]]) == 2
```

### 모의 테스트

#### [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

문제의 조건을 잘 이해 해야 하는 문제.  
우선 우리가 최대로 가질 수 있는 폰켓몬 수는 `len(nums) // 2` 이다  
운이 좋다면 저 갯수만큼 모두 서로 다른 종류일 수 있지만, 
그렇지 않을 수 있으므로 서로 다른 폰켓몬 수를 계산 한다 `len(set(nums))`
정답은 두 값 중 작은 값이 정답이 된다  

```python
from typing import List


def solution(nums: List[int]) -> int:
    possible_num_of_choices = len(nums) // 2
    return min(len(set(nums)), possible_num_of_choices)
```

#### [영어 끝말잇기](https://school.programmers.co.kr/learn/courses/30/lessons/12981)

마찬가지로 구현 문제에 가깝고, set 자료구조를 통해서 이미 사용된 단어인지 확인을 위해서 이번 챕터에 들어온 것으로 보인다  
문제 요구사항대로 이전 단어의 마지막 단어가 현재 단어의 첫 단어와 맞지 않거나, 이미 사용된 단어를 쓰는 경우  
index와 n 입력값을 통해 현재 몇 번째 라운드에서 몇 번째 참가자가 오답을 냈는 지 쉽게 계산 할 수 있다  
그 외의 경우 기본 값인 [0, 0]을 반환하면 되는 문제

```python
from itertools import islice
from typing import List


def solution(n: int, words: List[str]) -> List[int]:
    answer = [0, 0]
    used_words = {words[0]}
    previous_word = words[0]

    for index, word in islice(enumerate(words), 1, None):
        if previous_word[-1] != word[0] or word in used_words:
            return [index % n + 1, index // n + 1]

        used_words.add(word)
        previous_word = word

    return answer


assert solution(
    3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
) == [3, 3]
assert solution(
    5,
    [
        "hello",
        "observe",
        "effect",
        "take",
        "either",
        "recognize",
        "encourage",
        "ensure",
        "establish",
        "hang",
        "gather",
        "refer",
        "reference",
        "estimate",
        "executive",
    ],
) == [0, 0]
assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]
```

#### [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)

스트링을 정렬하고 그 특성을 이용해 앞에서부터 startswith에 걸리는 지 체크하면서 풀이  

```python
from typing import List


def solution(phone_book: List[str]) -> bool:
    sorted_phone_book = sorted(phone_book)
    index = 0

    while index < len(phone_book) - 1:
        if sorted_phone_book[index + 1].startswith(sorted_phone_book[index]):
            return False
        index += 1

    return True
```

다만 이 풀이 방식이 아니라 아래처럼 딕셔너리를 활용하는 방식도 있는 것 같다  
다만 윗 풀이보다 더 오래걸림. 아마도 string 만들고 하는 과정이 startswith 최적화 된 코드보다 느린게 아닌가 추측

```python
from typing import List


def solution(phone_book: List[str]) -> bool:
    phone_book_set = set(phone_book)
    for phone_number in phone_book:
        temp_list = []
        for char in phone_number:
            temp_list.append(char)
            temp_string = "".join(temp_list)
            if temp_string in phone_book_set and temp_string != phone_number:
                return False

    return True
```

#### [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)

모든 permutation을 계산하고 path의 합 중 최솟값을 찾는 나이브한 방법 -> 시간 초과 발생

```python
from itertools import permutations
from typing import List


def solution(n: int, costs: List[List[int]]) -> int:
    cost_by_path = {}
    for cost in costs:
        node1, node2, val = cost
        path = (node1, node2) if node1 < node2 else (node2, node1)
        cost_by_path[path] = val

    answer = sum(cost_by_path.values())
    for permutation in permutations(range(n)):
        path_cost = 0
        is_valid = True
        for i in range(len(permutation) - 1):
            node1 = permutation[i]
            node2 = permutation[i + 1]
            path = (node1, node2) if node1 < node2 else (node2, node1)

            if cost := cost_by_path.get(path):
                path_cost += cost
            else:
                is_valid = False
                break

        answer = min(answer, path_cost) if is_valid else answer

    return answer


assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
```

저자 풀이를 보고 조금 변형한 풀이  
우선 핵심은, 비용을 최소화 하는 것이기 때문에 사이클이 생기면 안된다 (왜냐면 최소 1 이상의 cost이므로 사이클이 생기면 무조건 최소보단 커짐)  
사이클의 판별은 두 개 노드의 root 노드가 같은지로 판단할 수 있다 (find 호출)  
코드 풀이에서 트리 압축과 rank를 활용한 부분도 있으니 이것도 챙겨갈 것  
이 문제는 그리고 사실 MST (최소 신장 트리)의 구현 문제와 같다
```python
from typing import List


def solution(n: int, costs: List[List[int]]) -> int:
    def find(node: int) -> int:
        if node == disjoint_set[node]:
            return node

        disjoint_set[node] = find(disjoint_set[node])
        return disjoint_set[node]

    def union(n1: int, n2: int) -> None:
        # find 과정을 통해 경로 압축이 이뤄짐
        root1 = find(n1)
        root2 = find(n2)

        if rank[root1] < rank[root2]:
            disjoint_set[root1] = root2
        elif rank[root1] > rank[root2]:
            disjoint_set[root2] = root1
        else:
            disjoint_set[root2] = root1
            rank[root1] += 1

    sorted_costs = sorted(costs, key=lambda c: c[2])
    disjoint_set = [x for x in range(n)]
    rank = [0] * n
    min_cost = 0
    num_of_edges = 0

    for cost_info in sorted_costs:
        if num_of_edges == n - 1:
            break

        node1, node2, cost = cost_info
        root_of_node1 = find(node1)
        root_of_node2 = find(node2)

        if root_of_node1 != root_of_node2:
            union(node1, node2)
            min_cost += cost
            num_of_edges += 1

    return min_cost


assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
```