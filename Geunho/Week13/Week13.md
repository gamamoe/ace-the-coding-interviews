# 16. 그리디 개념

## 16-4. 몸풀기 문제

### 거스름돈 주기

사용할 수 있는 코인이 서로 배수 관계이므로, 큰 숫자의 코인을 쓰는 경우 가짓수가 최소임이 보장됨  
즉, 최적 부분 구조를 만족하며, 마찬가지로 그리디 선택 속성을 만족  
따라서 큰 코인부터 사용할 갯수를 그리디하게 찾아서 채워나가는 식으로 풀이  

```python
from typing import List


def solution(amount: int) -> List[int]:
    answer = []
    current_amount = amount
    for coin in [100, 50, 10, 1]:
        num_of_coins, remainder = divmod(current_amount, coin)
        answer.extend([coin] * num_of_coins)
        current_amount = remainder

    return answer


assert solution(123) == [100, 10, 10, 1, 1, 1]
assert solution(350) == [100, 100, 100, 50]
```

### 부분 배낭 문제

0/1 배낭이 아니라 부분 배낭이므로, 무게 당 가치를 계산하여 정렬한 후 그 순서대로 weight_limit까지 채워넣으면서 풀이

```python
import math
from typing import List


def solution(items: List[List[int]], weight_limit: int) -> float:
    sorted_items = sorted(items, key=lambda item: item[1] / item[0], reverse=True)

    current_weight_limit = weight_limit
    answer = 0.0
    for weight, cost in sorted_items:
        if weight <= current_weight_limit:
            answer += cost
            current_weight_limit -= weight
        else:
            answer += current_weight_limit * (cost / weight)
            break

    return round(answer, 2)


assert math.isclose(solution([[10, 19], [7, 10], [6, 10]], 15), 27.33)
assert math.isclose(solution([[10, 60], [20, 100], [30, 120]], 50), 240)
```

## 16-5. 실전 문제

### [예산](https://school.programmers.co.kr/learn/courses/30/lessons/12982)

최대한 많은 부서를 지원해야하므로, 신청한 금액이 작은 순서대로 지원하면 결국 최적해가 된다  

```python
from typing import List


def solution(d: List[int], budget: int) -> int:
    d.sort()

    answer = 0
    remained_budget = budget
    for amount in d:
        if amount <= remained_budget:
            answer += 1
            remained_budget -= amount
        else:
            break

    return answer


assert solution([1, 3, 2, 5, 4], 9) == 3
assert solution([2, 2, 3, 3], 10) == 4
```

### [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

최대한 2명씩 태워야 최소한의 보트를 탑승하는 것이므로, 가장 무거운 사람과 가장 가벼운 사람을 페어가 가능한 형태로  
그리디하게 접근, 정렬을 한 후 left와 right를 적절하게 pointer를 갱신해주면 된다

```python
from typing import List


def solution(people: List[int], limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1

    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        answer += 1

    return answer


assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 80, 50], 100) == 3
```