### 배열 개념

인덱스와 값을 일대일 대응해 관리하는 자료구조  
인덱스만 알면 빠르게 탐색 가능 (Random access)

#### 배열 선언

```python
# 1차원 배열
vector = [0] * 6

# 2차원 배열 (e.g., 3 by 4 matrix)
matrix = [[0] * 3 for _ in range(4)] 
```

#### 배열 차원

중첩 리스트 형태로 다차원 배열을 표현 가능  
그러나 실제 메모리는 1차원 구조로 저장된다  
또한 2차원 배열을 1차원 배열로 표현해서 풀이하는 문제도 꽤 자주 출제됨  

```python
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2행 3열 원소
row_dim = 3
val1 = matrix1[1][2]
val2 = matrix2[1 * row_dim + 2]
```

#### 배열의 효율성

임의 접근 특징을 가지므로 데이터 접근의 시간 복잡도는 상수 시간복잡도 O(1)  
데이터 삽입은 마지막에 삽입 (append)는 상수 시간복잡도 그 외 처음 또는 중간 삽입은 선형 시간복잡도 O(N)  
데이터에 자주 접근하고 읽어야한다면 배열 사용을 고려해볼 수 있음  

* 배열로 표현하려는 데이터가 메모리에 할당 가능한지
* 중간에 데이터 삽입이 많은지

2가지를 고려해서 사용 여부를 판단하면 된다

### 자주 활용하는 리스트 기법

```python
# 맨 뒤에 데이터 추가
my_list = [1, 2, 3]
my_list.append(4)   # [1, 2, 3, 4]

# + 연산자로 데이터 추가
my_list = [1, 2, 3]
my_list = my_list + [4, 5] # [1, 2, 3, 4, 5]
# 또는 extend를 활용할 수 있음
my_list = my_list.extend([4, 5])

# pop 메서드
# 마지막 원소를 지우는 케이스 외에 인덱스를 받을 수 있으나 효율이 떨어짐
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop() # [1, 2, 3, 4]
```

Insert와 Remove 메서드는 존재는 하나 코딩 테스트에서는 효율 문제로 사용할 일이 거의 없을 것 같다

```python
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 9999) # [1, 2, 9999, 3, 4, 5]

# 제거하려는 값과 일치하는 처음 만나는 원소를 제거
my_list = [1, 2, 3, 2, 4, 5]
my_list.remove(2)   # [1, 3, 2, 4, 5]
```

그 외 리스트 컴프리헨션, len, index, sort, count 같은 메서드들도 자주 사용되는 메서드

### 배열 정렬하기

```python
from typing import List


def solution(arr: List[int]):
    return sorted(arr)
```

### 배열 제어하기

```python
from typing import List


def solution(arr: List[int]) -> List[int]:
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr, reverse=True)

    return sorted(sorted_arr, reverse=True)
```

### [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644)

조건이 매우 널널하므로 2중 루프로 가능한 경우를 찾고, 조건에 맞춰서 중복 제거 및 정렬하면 쉽게 해결 가능  
itertools의 조합 연산을 활용하는 코드도 있음

```python
from typing import List


# 2 <= len(numbers) <= 100
# 0 <= numbers[i] <= 100
def solution(numbers: List[int]) -> List[int]:
    num_of_elements = len(numbers)
    answer = set()
    for i in range(0, num_of_elements - 1):
        for j in range(i + 1, num_of_elements):
            answer.add(numbers[i] + numbers[j])

    return sorted(list(answer))
```

### [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

```python
from collections import defaultdict
from typing import List


def solution(answers: List[int]) -> List[int]:
    answer_rules = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    score_by_student_id = defaultdict(int)
    max_score = 0
    for student_id, rule in enumerate(answer_rules):
        for problem_id, answer in enumerate(answers):
            if answer == rule[problem_id % len(rule)]:
                score_by_student_id[student_id + 1] += 1

        max_score = max(max_score, score_by_student_id[student_id + 1])

    student_ids = {
        student_id: score
        for student_id, score in score_by_student_id.items()
        if score == max_score
    }.keys()
    return sorted(student_ids)


assert solution([1, 2, 3, 4, 5]) == [1]
assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
```

### [행렬의 곱셈](https://school.programmers.co.kr/learn/courses/30/lessons/12949)

```python
from typing import List


def solution(arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    answer = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


assert solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [
    [15, 15],
    [15, 15],
    [15, 15],
]
assert solution(
    [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
) == [
    [22, 22, 11],
    [36, 28, 18],
    [29, 20, 14],
]
```

### [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889)

```python
from collections import defaultdict
from typing import List


def solution(N: int, stages: List[int]) -> List[int]:
    sorted_stages = sorted(stages)
    stage_info_dict = defaultdict(int)
    for stage in sorted_stages:
        stage_info_dict[stage] += 1

    denominator = len(stages)
    failure_ratio_list = []
    for stage in range(1, N + 1):
        denominator -= stage_info_dict[stage - 1]

        if denominator == 0:
            failure_ratio_list.append((stage, 0.0))
        else:
            failure_ratio_list.append((stage, stage_info_dict[stage] / denominator))

    return [e[0] for e in sorted(failure_ratio_list, key=lambda x: (-x[1], x[0]))]
```

### [방문 길이](https://school.programmers.co.kr/learn/courses/30/lessons/49994)

frozenset을 활용하거나 양방향 경로로 간주해서 2가지 케이스 모두 집어넣는 방식 둘 다 활용 가능

```python
def solution(dirs: str) -> int:
    delta_by_direction = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    visited_path = set()
    current_coordinate = (0, 0)
    for direction in dirs:
        x, y = current_coordinate
        dx, dy = delta_by_direction[direction]
        next_coordinate = (x + dx, y + dy)

        if -5 <= next_coordinate[0] <= 5 and -5 <= next_coordinate[1] <= 5:
            path = frozenset([current_coordinate, next_coordinate])

            if path not in visited_path:
                visited_path.add(path)

            current_coordinate = next_coordinate

    return len(visited_path)


assert solution("UD") == 1
assert solution("ULURRDLLU") == 7
assert solution("LULLLLLLU") == 7
```

### [배열 뒤집기](https://school.programmers.co.kr/learn/courses/30/lessons/120821)

Slicing을 활용하는 것은 생각하지 못했는데, 더 간결하고 의미도 명확해보임

```python
from typing import List


def solution(num_list: List[int]) -> List[int]:
    # return num_list[::-1]
    return list(reversed(num_list))


assert solution([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert solution([1, 1, 1, 1, 1, 2]) == [2, 1, 1, 1, 1, 1]
assert solution([1, 0, 1, 1, 1, 3, 5]) == [5, 3, 1, 1, 1, 0, 1]
```

### [나누어 떨어지는 숫자 배열](https://school.programmers.co.kr/learn/courses/30/lessons/12910)

요구사항대로 구현하면 되는 문제

```python
from typing import List


def solution(arr: List[int], divisor: int) -> List[int]:
    divisible_elements = [x for x in arr if x % divisor == 0]
    answer = sorted(divisible_elements) if divisible_elements else [-1]
    return answer
```

다만 반환 시 or를 활용해 더 간단하게 아래와 같이도 가능하다

```python
from typing import List


def solution(arr: List[int], divisor: int) -> List[int]:
    divisible_elements = [x for x in arr if x % divisor == 0]
    return sorted(divisible_elements) or [-1]
```