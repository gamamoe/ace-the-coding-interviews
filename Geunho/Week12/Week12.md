# 15. 동적 계획법

## 15-1. 동적 계획법 개념

동적 계획법은 전체 문제를 한 번에 해결하는 것이 아니라, 작은 부분 문제를 해결하고, 이것을 활용하여 전체 문제를 해결하는 방법  
이 때 동적계획법이 효율적이려면 다음과 같은 조건들이 필요하다

* 큰 문제를 작은 문제로 나누었을 때 동일한 작은 문제가 반복해서 등장해야 함 (중복 부분 문제)
* 큰 문제의 해결책은 작은 문제의 해결책의 합으로 구성할 수 있어야 함 (최적 부분 구조)

### 점화식 세우기와 동적 계획법

동적 계획법으로 문제를 해결하는 절차는 다음과 같다

1. 문제를 해결하는 해가 이미 있다고 가정
2. 종료 조건을 설정
3. 과정 1, 2를 활용해 점화식을 만든다

```
Fact(N):    # 문제를 해결하는 해
   if (N == 1) return 1 # 종료 조건
   else Fact(N - 1) * N # 점화식 일반항
```

재귀 호출의 호출 수가 늘어나면 메모리 문제가 생길 수 있고, 이를 재귀 호출의 횟수를 줄이는 메모이제이션을 사용할 수 있음  
대표적인 예를 들면 피보나치 함수 계산 방법이 있을 수 있다  

```
dp = [0...len(N)]
Fibo(N):    # 문제를 해결하는 해
    if dp[N]: return dp[N]  # 메모이제이션
    if N == 1 or N == 2: dp[N] = 1  # 메모이제이션 + 종료 조건
    else dp[N] = dp[N - 1] + dp[N - 2]  # 메모이제이션 + 점화식 일반항
  
return dp[N] 
```

## 15-2. 몸풀기 문제

### LCS 길이 계산하기

초기값 0으로 설정 후 2중 loop 순회하면서 문자가 같을 때와 다를 때를 나눠서 dp 테이블을 채우고 최종적으로 결과 반환

```python
def solution(str1: str, str2: str) -> int:
    str1_len = len(str1)
    str2_len = len(str2)
    dp = [[0] * (str1_len + 1) for _ in range(str2_len + 1)]

    for i in range(str2_len):
        for j in range(str1_len):
            if str2[i] == str1[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[str2_len][str1_len]


assert solution("ABCBDAB", "BDCAB") == 4
assert solution("AGGTAB", "GXTXAYB") == 4
```

### LIS 길이 계산하기

초기값 설정 후 앞에서 조건 만족하는 후보군 중 가장 큰 값의 +1로 dp 테이블을 계속 갱신

```python
from typing import Sequence


def solution(nums: Sequence[int]) -> int:
    num_of_elements = len(nums)
    dp = [0] * num_of_elements
    dp[0] = 1

    for index in range(1, num_of_elements):
        candidates = [dp[i] for i, x in enumerate(nums[:index]) if x < nums[index]]
        dp[index] = max(candidates) + 1 if candidates else 1

    return max(dp)


assert solution([1, 4, 2, 3, 1, 5, 7, 3]) == 5
assert solution([3, 2, 1]) == 1
```

### 조약돌 문제 

초항이 네 가지 패턴이 있다는 점과, 네 가지 경우에 대해서 max 값을 앞에서부터 갱신해나가는 점화식 세우는 것이 포인트  
쉽지는 않다

```python
from typing import Sequence


def solution(arr: Sequence[Sequence[int]]) -> int:
    num_of_cols = len(arr[0])
    dp = [[0] * num_of_cols for _ in range(4)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = arr[2][0]
    dp[3][0] = arr[0][0] + arr[2][0]

    for i in range(1, num_of_cols):
        dp[0][i] = arr[0][i] + max(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = arr[1][i] + max(dp[0][i - 1], dp[2][i - 1], dp[3][i - 1])
        dp[2][i] = arr[2][i] + max(dp[0][i - 1], dp[1][i - 1])
        dp[3][i] = arr[0][i] + arr[2][i] + dp[1][i - 1]

    return max(dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1])


assert solution([[1, 3, 3, 2], [2, 1, 4, 1], [1, 5, 2, 3]]) == 19
assert solution([[1, 7, 13, 2, 6], [2, -4, 2, 5, 4], [5, 3, 5, -3, 1]]) == 32
```

## 실전 문제

### [피보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945)

너무 전형적인 DP 문제, modulo 처리를 해주는 부분만 신경쓰면 어렵지 않게 풀이 가능

```shell
def solution(n: int) -> int:
    dp = [0] * 100_001
    dp[1] = 1

    modulo = 1234567
    for index in range(2, n + 1):
        dp[index] = (dp[index - 1] % modulo + dp[index - 2] % modulo) % modulo

    return dp[n]
```

### [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900)

그림을 그리면서 규칙을 찾자  
`dp[1]` 길이가 1을 만족하는 경우는 세로 막대 하나인 **1가지**  
`dp[2]` 길이가 2를 만족하는 경우는 세로 막대 2개 또는 가로 막대 2개인 **2가지**
그 후 n에 대해서는 일반화를 바로 앞 항 (n - 1)에서 세로 막대를 하나씩 붙이거나, 2항 앞인 (n - 1)에서 가로 막대 2개를 붙이는 경우의 합  
따라서 피보나치 수열과 거의 유사하게 계산할 수 있다

```python
def solution(n: int) -> int:
    dp = [0] * 60_001
    dp[1] = 1
    dp[2] = 2

    modulo = 1_000_000_007
    for index in range(3, n + 1):
        dp[index] = (dp[index - 1] % modulo + dp[index - 2] % modulo) % modulo

    return dp[n]


assert solution(4) == 5
```

### [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)

위에서부터 최대가 되는 합을 계산해서 저장해두고, 다음 층에서 앞에서 계산한 층의 정보를 활용하는 DP문제

```python
from typing import Sequence


def solution(triangle: Sequence[Sequence[int]]) -> int:
    height = len(triangle)
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])


assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
```

### [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913)

정수 삼각형 문제와 유사함, 위에서부터 누적합 방식으로 dp 테이블을 채워나가는 식으로 풀이

```python
from typing import List


def solution(land: List[List[int]]) -> int:
    num_of_rows = len(land)
    num_of_cols = 4
    for row_index in range(1, num_of_rows):
        for col_index in range(num_of_cols):
            land[row_index][col_index] = max(
                [
                    x + land[row_index][col_index]
                    for i, x in enumerate(land[row_index - 1])
                    if i != col_index
                ]
            )

    return max(land[-1])


assert solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16
```
### [가장 큰 정사각형 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12905)

정사각형의 성질을 이용해서 1개, 2개, 3개가 1x1 3개, 2x2 3개, ... 반복하면서 큰 사각형을 만들 수 있다는 점이 아이디어  
처음 DP로 접근하는 것이 쉽지는 않은 것 같다

```python
from typing import List


def solution(board: List[List[int]]) -> int:
    num_of_rows = len(board)
    num_of_cols = len(board[0])

    for row_index in range(1, num_of_rows):
        for col_index in range(1, num_of_cols):
            if board[row_index][col_index] == 1:
                board[row_index][col_index] = (
                    min(
                        board[row_index][col_index - 1],
                        board[row_index - 1][col_index - 1],
                        board[row_index - 1][col_index],
                    )
                    + 1
                )

    max_len = max([max(row) for row in board])
    return max_len**2


assert solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]) == 9
assert solution([[0, 0, 1, 1], [1, 1, 1, 1]]) == 4
```

### [단어 퍼즐](https://school.programmers.co.kr/learn/courses/30/lessons/12983)

앞에서부터 무식하게 조각 수를 카운팅하는 방식에서 발전해서 가능한 토큰의 길이를 활용해서 dp 테이블을 세우는 문제  
본문에도 있지만 문자열이랑 결합한 문제라 쉽지 않다

```python
import math
from typing import Sequence


def solution(strs: Sequence[str], t: str) -> int:
    n = len(t)
    dp = [math.inf] * (n + 1)
    dp[0] = 0
    sizes = set(len(s) for s in strs)
    str_set = set(strs)
    for i in range(1, n + 1):
        for size in sizes:
            if i - size >= 0 and t[i - size : i] in str_set:
                dp[i] = min(dp[i], dp[i - size] + 1)

    return dp[n] if dp[n] < math.inf else -1


assert solution(["ba", "na", "n", "a"], "banana") == 3
assert solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple") == 2
assert solution(["ba", "an", "nan", "ban", "n"], "banana") == -1
```