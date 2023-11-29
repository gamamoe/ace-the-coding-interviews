

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