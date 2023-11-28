

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
