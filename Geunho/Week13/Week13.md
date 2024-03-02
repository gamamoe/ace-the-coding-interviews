# 16. 그리디 개념

그리디 -> 문제 해결 과정에서 순간마다 최선의 선택을 하며 선택을 번복하지 않는 알고리즘  
다시 말해서 지역 최적해를 추구한다라고 말할 수 있다  
그리디 알고리즘이 최적해를 보장하려면 

- 최적 부분 구조 (Optimal substructure): 부분해를 푸는 과정이 최적해를 구하는 과정과 일치
- 그리디 선택 속성 (Greddy selection property): 선택 과정이 다른 과정에 영향을 주지 않음

이런 특징때문에 항상 최적해를 구할 수 있다는 보장은 못하지만, 빠르게 근사해를 제공하는 효과는 누릴 수가 있다

앞에서 공부했던 Union-Find를 활용하여 최소 신장 트리를 구하는 알고리즘도 그리디 알고리즘의 일종  
짐을 쪼갤 수 있는 배낭 문제도 흔히 알려진 그리디 알고리즘을 활용할 수 있는 예제 중 하나

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

### [귤 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/138476)

종류를 최소화 하는 것이 목적이므로, 사이즈별로 빈도를 세고 빈도가 낮은 사이즈부터 걸러내는 식으로 그리디하게 접근  
바꿔 생각하면 특정 사이즈에 빈도가 많다면 골라냈을 때 이득이 없다는 것을 캐치하면 쉽게 풀이 가능하다

```python
import collections
from typing import Sequence


def solution(k: int, tangerine: Sequence[int]) -> int:
    count_by_size = collections.Counter(tangerine)
    sorted_sizes = sorted(count_by_size.keys(), key=lambda x: count_by_size[x])

    num_of_tangerines = len(tangerine) - k
    for size in sorted_sizes:
        if count_by_size[size] > num_of_tangerines:
            break

        num_of_tangerines -= count_by_size[size]
        count_by_size.pop(size)

    return len(count_by_size)


assert solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3
assert solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2
assert solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1
```

### [기지국 설치](https://school.programmers.co.kr/learn/courses/30/lessons/12979)

정확성은 다 통과하지만 효율성에서 통과되지 않는 풀이

```python
from typing import Sequence


def solution(n: int, stations: Sequence[int], w: int) -> int:
    coverages = [False] * n
    for station in stations:
        start = max(0, station - 1 - w)
        end = min(station -1 + w, n - 1)

        for index in range(start, end + 1):
            coverages[index] = True

    answer = 0
    temp_container = []
    for index in range(n):
        if coverages[index]:
            if temp_container:
                temp_container = []
                answer += 1
        else:
            if len(temp_container) < 2 * w + 1:
                temp_container.append(index)
            else:
                temp_container = [index]
                answer += 1

    return answer + 1 if temp_container else answer


assert solution(11, [4, 11], 1) == 3
assert solution(16, [9], 2) == 3
```

1부터 순서대로 이동하면서 해당 좌표가 설치된 기지국의 바운더리에 있는 지 없는 지 확인하면서 좌표를 업데이트  
해당 좌표가 기지국 바운더리에 없으면 loc - w < loc < loc + w를 커버할 수 있도록 하고 좌표를 업데이트  
해당 좌표가 기지국 바운더리에 있다면, 기지국이 설치된 위치 + w + 1로 좌표를 업데이트하면 빠짐 없이 커버가 가능해진다  

```python
from typing import Sequence


def solution(n: int, stations: Sequence[int], w: int) -> int:
    location = 1
    answer = 0
    station_index = 0
    while location <= n:
        if station_index < len(stations) and location >= stations[station_index] - w:
            location = stations[station_index] + w + 1
            station_index += 1
        else:
            location += 2 * w + 1
            answer += 1

    return answer


assert solution(16, [9], 2) == 3
assert solution(11, [4, 11], 1) == 3
```