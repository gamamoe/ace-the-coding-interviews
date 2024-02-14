### 정렬 개념

정렬이란 사용자가 정의한 순서로 데이터를 나열하는 것

- 오름차순
- 내림차순
- 임의의 조건

정렬이 된 데이터에서는 원하는 데이터를 쉽게 찾을 수 있기 때문에 효율적

#### 병합 정렬

전형적인 분할-정복 방식의 정렬 알고리즘  
매 과정에서 반씩 분할 후, 분할된 데이터의 크기가 1일 때부터 정렬된 순서로 합병하는 방식

#### 힙 정렬

힙의 특징을 이용해서 최솟값 또는 최댓값을 반복적으로 pop하면 결국 정렬된 데이터를 얻을 수 있게됨  
파이썬에서는 heapq의 여러가지 메서드를 활용해서 우선순위 큐 연산들을 지원할 수 있다  

#### 위상 정렬

방향이 있고 cycle이 없는 graph (DAG)에서 태스크의 순서를 정렬하는 알고리즘  
각 노드로 들어오는 input stream의 차수를 기준으로 초기화를 하고, 큐를 이용해서 집어넣은 후  
차수가 0인 노드를 팝하면서 downstream으로 연결된 노드의 차수를 -1씩 감소하면서 반복  

#### 계수 정렬

카운팅 정렬이라고도 불리며, 몇 가지 한계 케이스 (음수 또는 sparse 배열, 너무 큰 range)가 아닌 경우  
효율적으로 정렬이 가능함 (비교 정렬과 다르게 선형시간에 정렬 가능)

### 몸풀기 문제

#### 계수 정렬 구현하기

문제 조건에서 알파벳 소문자라는 조건이 있으므로, 작은 범위만 볼 수 있으므로 계수 정렬을 적용할 수 있는 좋은 예제  
Python의 ord나 chr 함수를 알아야 쉽게 풀이 가능

```python
def solution(s: str) -> str:
    counts = [0] * 26
    for char in s:
        counts[ord(char) - ord("a")] += 1

    answer = []
    for index, count in enumerate(counts):
        for _ in range(count):
            answer.append(chr(index + ord("a")))

    return "".join(answer)


assert solution("hello") == "ehllo"
assert solution("algorithm") == "aghilmort"
```

#### 정렬이 완료된 두 배열 합치기

교재 풀이와 거의 유사함, 다만 arr1 또는 arr2 중 하나가 끝났다면, 간단하게 extend를 활용해서 붙이는 부분만 조금 차이

```python
from typing import Sequence, List


def solution(arr1: Sequence[int], arr2: Sequence[int]) -> List[int]:
    answer = []

    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] <= arr2[ptr2]:
            answer.append(arr1[ptr1])
            ptr1 += 1
        else:
            answer.append(arr2[ptr2])
            ptr2 += 1

    if ptr1 == len(arr1):
        answer.extend(arr2[ptr2:])
    else:
        answer.extend(arr1[ptr1:])

    return answer


assert solution([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
assert solution([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
```

### 실전 문제

#### [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915)

문제 조건대로 정렬 비교 함수를 구현하면 쉽게 풀 수 있는 문제  
인덱스 n의 문자가 같은 경우 사전순으로 앞선 문자열이 앞쪽에 위치한다는 부분을 놓치지 말 것

```python
from typing import Sequence, List


def solution(strings: Sequence[str], n: int) -> List[str]:
    return sorted(strings, key=lambda s: (s[n], s))


assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
```

#### [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

우선 입력으로 들어온 n을 string으로 변환 후 내림차순으로 정렬  
정렬된 결과를 join으로 묶어서 string으로 만든 후 최종적으로는 int로 변환해서 반환

```python
def solution(n: int) -> int:
    return int("".join(sorted(str(n), reverse=True)))


assert solution(118372) == 873211
```

#### [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

slicing 연산으로 배열을 잘라내고, 정렬 후 인덱스 결과만 저장하면 쉽게 풀이 가능한 문제  
인덱스 시작이 0이 아니라 1이므로 off-by-one error만 주의

```python
from typing import Sequence, List


def solution(array: Sequence[int], commands: Sequence[Sequence[int]]) -> List[int]:
    answer = []
    for i, j, k in commands:
        sorted_sub_array = sorted(array[i - 1:j])
        answer.append(sorted_sub_array[k - 1])
    return answer
```

#### [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)

파이썬에서 제공하는 cmp_to_key 를 활용해서 문제 조건에 맞게 사용자 정의 정렬을 하는 연습 문제  
a가 b보다 선이라면 음수 값을, 동등하다면 0을, a가 b보다 후라면 양수 값을 반환하는 식으로 cmp 함수를 작성하면 된다  
reference: https://docs.python.org/ko/3/library/functools.html#functools.cmp_to_key

> A comparison function is any callable that accepts two arguments, compares them, 
> and returns a negative number for less-than, zero for equality, or a positive number for greater-than. 
> A key function is a callable that accepts one argument and returns another value to be used as the sort key.

```python
from functools import cmp_to_key
from typing import Sequence


def solution(numbers: Sequence[int]) -> str:
    def _compare(a: int, b: int) -> int:
        c1 = f"{a}{b}"
        c2 = f"{b}{a}"
        return int(c1) - int(c2)

    sorted_numbers = sorted(numbers, key=cmp_to_key(_compare), reverse=True)
    answer = "".join(str(x) for x in sorted_numbers)
    return "0" if int(answer) == 0 else answer


assert solution([6, 10, 2]) == "6210"
assert solution([3, 30, 34, 5, 9]) == "9534330"
assert solution([0, 0, 0]) == "0"
```

#### [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)

문자열을 스택 자료구조를 이용해서 파싱하는 식으로 진행했는데 조금 더 간결하게 작성가능할 것 같다

```python
from collections import deque
from typing import List


def solution(s: str) -> List[int]:
    stack = []
    candidates = []
    temp_container = []
    for token in s[1:-1]:
        if token == "{":
            stack.append(token)
        elif token == "}":
            stack.append("".join(temp_container))
            temp_container.clear()

            queue = deque()
            while (element := stack.pop()) != "{":
                queue.appendleft(int(element))
            candidates.append(set(queue))
        elif token == ",":
            stack.append("".join(temp_container))
            temp_container.clear()
        elif token.isdigit():
            temp_container.append(token)
        else:
            continue

    candidates.sort(key=lambda c: len(c))
    previous_set = candidates[0]
    answer = [min(previous_set)]
    for candidate in candidates[1:]:
        answer.append(min(candidate.difference(previous_set)))
        previous_set = candidate

    return answer


assert solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
assert solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
assert solution("{{20,111},{111}}") == [111, 20]
assert solution("{{123}}") == [123]
assert solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]
```

문자열 처리를 이용해서 좀 더 간결하게 풀이한 코드

```python
from typing import List


def solution(s: str) -> List[int]:
    prepared_str = s.lstrip("{").rstrip("}")
    tuple_set = [set(term.split(",")) for term in prepared_str.split("},{")]
    tuple_set.sort(key=lambda _tuple: len(_tuple))

    answer = [min(tuple_set[0])]
    prev = tuple_set[0]
    for x in tuple_set[1:]:
        answer.append(min(x.difference(prev)))
        prev = x

    return [int(x) for x in answer]
```

#### [지형 이동](https://school.programmers.co.kr/learn/courses/30/lessons/62050)

최소 비용, 그리고 인접한 노드끼리 이동 가능하다는 점에서 BFS를 떠올리고, 
이동 비용이 작은 순으로 방문 처리를 하므로 우선순위 큐를 착안할 수 있어야한다  
원점부터 시작하여 상, 하, 좌, 우 인접한 칸의 cost와 좌표를 우선순위 큐에 넣고  
우선순위 큐에서 cost가 작은 순으로 뽑아 내고 또 상, 하, 좌, 우 탐색  
방문처리 하는 시점은 일반적인 BFS와 좀 다르므로 유의할 것

```python
import heapq
from typing import Sequence


def solution(land: Sequence[Sequence[int]], height: int) -> int:
    dimension = len(land)
    visited = [[False] * dimension for _ in range(dimension)]
    start = (0, 0, 0)  # cost, row, col
    queue = [start]
    heapq.heapify(queue)

    answer = 0
    while queue:
        cost, row, col = heapq.heappop(queue)

        if visited[row][col]:
            continue

        answer += cost
        visited[row][col] = True
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + drow, col + dcol

            if (
                0 <= new_row < dimension
                and 0 <= new_col < dimension
                and not visited[new_row][new_col]
            ):
                if (diff := abs(land[row][col] - land[new_row][new_col])) <= height:
                    heapq.heappush(queue, (0, new_row, new_col))
                else:
                    heapq.heappush(queue, (diff, new_row, new_col))

    return answer


assert (
    solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3) == 15
)
assert (
    solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)
    == 18
)
```

### 추가 문제

#### [파일명 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/17686)

문제 요구사항대로 구현, TAIL이 빈 문자일 수 있으므로 해당 부분을 주의해야 함

```python
from typing import Sequence, List


def solution(files: Sequence[str]) -> List[str]:
    custom_files = []
    for original_order, file_name in enumerate(files):
        head = []
        index = 0
        while not file_name[index].isdigit():
            head.append(file_name[index])
            index += 1
        head = "".join(head)

        number = []
        while index < len(file_name) and file_name[index].isdigit():
            number.append(file_name[index])
            index += 1
        number = "".join(number)
        tail = file_name[index:]
        custom_files.append((head, number, tail, original_order))

    custom_files.sort(key=lambda file: (file[0].lower(), int(file[1]), file[3]))
    return [f"{head}{number}{tail}" for head, number, tail, _ in custom_files]
```

#### [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

```python
from collections import Counter
from typing import Sequence


def solution(citations: Sequence[int]) -> int:
    citation_counter = Counter(citations)
    sorted_citations = sorted(citations, reverse=True)

    h_index = {}
    accumulative_sum = 0
    answer = 0
    for citation in sorted_citations:
        if citation in h_index:
            continue

        accumulative_sum += citation_counter[citation]
        h_index[citation] = accumulative_sum

        if citation >= accumulative_sum:
            answer = max(answer, accumulative_sum)

    return answer


assert solution([3, 0, 6, 1, 5]) == 3
assert solution([0, 0, 0, 0, 0]) == 0
assert solution([0, 0, 0, 0, 1]) == 1
assert solution([9, 9, 9, 12]) == 4
```
