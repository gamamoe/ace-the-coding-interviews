# 14. 시뮬레이션

## 시뮬레이션 문제 풀이 노하우

### 시뮬레이션 문제를 푸는 방법

성능에 중점을 둔 앞 장과 다르게, 시뮬레이션은 구현에 중점을 맞추는 유형이다  
다른 알고리즘도 그렇지만 시뮬레이션 문제는 특히 아래 두 가지를 염두에 두고 문제 풀이에 접근  

- 하나의 문제를 최대한 여러 개로 분리
- 예외 처리가 필요한 부분은 독립 함수로 구현

### 행렬 연산

지문에 꼭 행렬 내용이 없더라도, 행렬 연산을 활용해서 풀이할 수 있을 수 있으므로 몇 가지 연산들을 기억해두자  

* 행렬 덧셈과 뺄셈, 그리고 곱셈
* 전치 행렬

### 좌표 연산

이전 장에서 했던 `arr[row][col]` 또는 `arr[y][x]` 형태로 주로 표현  
이동 역시 dy, dx 같은 오프셋을 활용하면 실수를 줄일 수 있다  

### 대칭, 회전 연산

행렬에서의 대칭, 회전 연산인데, 몇 가지 예제만 손으로 해보면 규칙을 발견할 수 있음  
가령 3x3 행렬의 좌우 대칭은 `A[i, j] = A[i, (N - 1) - j]`, 상하대칭은 `A[i, j] = A[(N - 1) - i, j]`와 같이 일반화 가능

## 몸풀기 문제

### 배열 회전하기

손으로 써보고 규칙을 파악해서 구현하는 문제. rotate라는 함수를 따로 분리하는 부분을 기억해두면 좋음  
책에서는 원본 배열을 수정하지 않기 위해서 copy를 하는 데 이런 부분도 하나 챙겨가면 좋다

```python
from typing import List


def solution(arr: List[List[int]], n: int) -> List[List[int]]:
    def rotate(_arr: List[List[int]]) -> List[List[int]]:
        placeholder = [[0] * dim for _ in range(dim)]

        for row in range(dim):
            for col in range(dim):
                placeholder[col][dim - 1 - row] = _arr[row][col]

        return placeholder

    if n == 4:
        return arr

    dim = len(arr)
    rotated_arr = arr
    for _ in range(n):
        rotated_arr = rotate(rotated_arr)

    return rotated_arr


assert solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1) == [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4],
]
assert solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2) == [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1],
]
```

### 두 행렬을 곱한 후 전치 행렬 만들기

문제는 3x3 조건이라 좀 더 나이브하게 구현 가능함, 다만 일반화까지 고려한 코드로 작성했음 (예외처리 x)

```python
from typing import List, Sequence


def solution(
    matrix1: Sequence[Sequence[int]], matrix2: Sequence[Sequence[int]]
) -> List[List[int]]:
    def matmul() -> List[List[int]]:
        n, p, m = len(matrix1), len(matrix1[0]), len(matrix2[0])

        placeholder = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    placeholder[i][k] += matrix1[i][j] * matrix2[j][k]

        return placeholder

    def transpose(matrix: Sequence[Sequence[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        placeholder = [[0] * n for _ in range(m)]
        for row in range(n):
            for col in range(m):
                placeholder[row][col] = matrix[col][row]
        return placeholder

    matmul_result = matmul()
    answer = transpose(matmul_result)
    return answer


assert solution(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
) == [[30, 84, 138], [24, 69, 114], [18, 54, 90]]
assert solution(
    [[2, 4, 6], [1, 3, 5], [7, 8, 9]], [[9, 1, 2], [4, 5, 6], [7, 3, 8]]
) == [[76, 56, 158], [40, 31, 74], [76, 60, 134]]
```

### 달팽이 수열 만들기

1) 값을 채우는 부분이 valid 한지 (가능한 좌표를 벗어나지 않고 방문하지 않았는 지)
2) 1)에서 valid하다면 해당 좌표에 값을 채우고 방문 처리
3) 1)에서 invalid하다면 방향을 전환해야한다는 의미이므로 다음 방향값을 가져와서 신규 좌표로 갱신
4) 이것을 n x n 행렬을 다 채울 때까지 반복

```python
from typing import List


def solution(n: int) -> List[List[int]]:
    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < n and 0 <= col < n and not visited[row][col]

    def get_direction(direction: str) -> str:
        next_direction_by_current_direction = {"R": "D", "D": "L", "L": "U", "U": "R"}
        return next_direction_by_current_direction[direction]

    def get_offset(direction: str):
        if direction == "R":
            return 0, 1
        elif direction == "D":
            return 1, 0
        elif direction == "L":
            return 0, -1
        else:  # "U"
            return -1, 0

    answer = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    current_row, current_col = 0, -1
    current_direction = "R"
    start = 1
    while start <= n * n:
        drow, dcol = get_offset(current_direction)
        if not is_valid(current_row + drow, current_col + dcol):
            current_direction = get_direction(current_direction)
            drow, dcol = get_offset(current_direction)

        current_row = current_row + drow
        current_col = current_col + dcol
        answer[current_row][current_col] = start
        visited[current_row][current_col] = True
        start += 1

    return answer


assert solution(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert solution(4) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
```

## 실전 문제

### [이진 변환](https://school.programmers.co.kr/learn/courses/30/lessons/70129)

1) 변환 시 제거되는 0의 갯수 세기
2) 남은 길이 정수값을 다시 이진법으로 나타낸 문자열로 변경

이 과정을 쪼개서 생각하는 게 핵심
갯수 세기는 아래 코드와 다르게 `s.count("0")`으로 간단하게 가능했고,  
이진변환은 보통 `bin()`을 사용하는 데 이 경우 앞에 `0b` 접두사가 붙는다  
format 스트링을 활용하면 이런 부분도 깔끔하게 회피 가능

```python
from typing import List


def solution(s: str) -> List[int]:
    num_of_transformation = 0
    num_of_zeros = 0
    while s != "1":
        zero_counts = len([digit for digit in s if digit == "0"])
        len_after_transform = len(s) - zero_counts
        s = f"{len_after_transform:b}"
        num_of_transformation += 1
        num_of_zeros += zero_counts

    return [num_of_transformation, num_of_zeros]


assert solution("110010101001") == [3, 8]
assert solution("01110") == [3, 3]
assert solution("1111111") == [4, 1]
```

### [롤케이크 자르기](https://school.programmers.co.kr/learn/courses/30/lessons/132265)

앞에서부터 자르고, 토핑의 종류를 비교하는 구현  
왼쪽 토핑 종류와 오른쪽 토핑 종류를 저장할 counter 객체를 만든 후 슬라이딩하면서 넣고 빼면서 key의 갯수를 확인하는 식으로 풀이

```python
from collections import Counter
from typing import Sequence


def solution(topping: Sequence[int]) -> int:
    answer = 0

    left_toppings = Counter()
    right_toppings = Counter(topping)
    for _topping in topping:
        left_toppings[_topping] += 1
        right_toppings[_topping] -= 1
        
        if right_toppings[_topping] == 0:
            right_toppings.pop(_topping)

        if len(left_toppings) == len(right_toppings):
            answer += 1

    return answer
```
