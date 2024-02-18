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
