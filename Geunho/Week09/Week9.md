### 백트래킹

#### 백트래킹과 백트래킹 알고리즘 개념

깊이 우선 탐색, 너비 우선 탐색은 데이터를 전부 확인하는 방법이며 이를 완전 탐색이라고 함  
완전 탐색은 모든 경우의 수를 탐색하는 방법이므로 비효율적  
따라서 탐색을 하다가 가능성이 없다면 되돌아가고, 가능성이 있는 곳을 탐색하는 알고리즘을 백트래킹이라고 한다

백트래킹 알고리즘의 핵심은 '해가 될 가능성을 판단하는 것'이며 그것을 유망함수라는 것을 정의하여 판단함

1. 유효한 해의 집합을 정의
2. 위 단계에서 정의한 집합을 그래프로 표현
3. 유망 함수를 정의
4. 백트래킹 알고리즘을 활용해서 해를 찾음

예를 들어 1, 2, 3, 4 중 2개의 숫자를 뽑아서 6보다 큰 조합을 찾을 때 백트래킹을 활용한다면  
유망 함수로는 처음 숫자가 3 미만이면 백트래킹한다라는 전략으로 접근 가능  
또는 부분 집합의 합이 K가 되는 경우를 구할 때 완전 탐색은 포함/미포함 경우의 수로 봤을 때 2^n 이지만  
백트래킹을 활용한다면 1) 합이 K가 되면 더 탐색하지 않고 2) 현재까지의 합이 K 이상이라면 더 탐색하지 않을 수 있음

### 몸풀기 문제

#### 1부터 N까지 숫자 중 합이 10이 되는 조합 구하기

유망 함수의 조건

1. 합이 10이 되는 경우 바로 return 및 결과에 추가
2. 숫자의 합이 10보다 크면 백트래킹

0부터 시작해서 제일 하단의 backtrack은 아래와 같이 퍼지는 형태. 즉 유효한 해의 집합을 구성하는 코드 연습이 필요함 
```python
# [1] -> [1, 2]
#        [1, 3]
#        [1, 4]
#        ...
#        [1, N]
# [2] -> [2, 3]
#     -> [2, 4]
#     -> [2, 5]
#        ...
# [3] -> [3, 4]
#        ...
# ...
# [7] -> [7, 8]
#        ...
```

```python
from typing import List


def solution(N: int) -> List[List[int]]:
    results = []

    def backtrack(total_sum: int, path: List[int], start: int):
        if total_sum == 10:
            results.append(path)
            return

        for i in range(start, N + 1):
            if total_sum + i <= 10:
                backtrack(total_sum + i, path + [i], i + 1)

    backtrack(0, [], 1)
    return results


assert solution(5) == [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
assert solution(2) == []
assert solution(7) == [
    [1, 2, 3, 4],
    [1, 2, 7],
    [1, 3, 6],
    [1, 4, 5],
    [2, 3, 5],
    [3, 7],
    [4, 6],
]
```

### 실전 문제

#### [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)

```python
from itertools import permutations
from typing import List


def solution(k: int, dungeons: List[List[int]]) -> int:
    answer = -1
    for permutation in permutations([x for x in range(len(dungeons))]):
        current_val = k
        num_of_dungeon = 0
        for index in permutation:
            if current_val >= dungeons[index][0]:
                num_of_dungeon += 1
                current_val -= dungeons[index][1]
        answer = max(answer, num_of_dungeon)

    return answer


assert solution(80, [[80, 20], [50, 40], [30, 10]]) == 3
```

#### [N-Queen](https://school.programmers.co.kr/learn/courses/30/lessons/12952)

(0, 0)부터 시작해서 상태 트리를 그리고 구현에 옮기는 연습이 필요  
현재 행 정보와, 체스판에 놓은 좌표를 들고 갱신하며 현재 행이 마지막 행까지 온 경우 퀸을 놓을 수 있는 경우이다  
말판을 놓을 때 탐색에 들어가는 조건은 같은 열이 아니고, 대각선에 위치하지 않을 때만 탐색에 들어간다  

```python
from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    row: int
    col: int


def solution(n: int) -> int:
    answer = []

    def search(row: int, coordinates: List[Coordinate]):
        if row == n:
            answer.append(1)
            return

        for col in range(n):
            early_return = False
            for coord in coordinates:
                prev_row, prev_col = coord.row, coord.col
                if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                    early_return = True
                    break

            if not early_return:
                search(row + 1, coordinates + [Coordinate(row, col)])

    search(0, [])
    return len(answer)


assert solution(4) == 2
```

#### [양궁대회](https://school.programmers.co.kr/learn/courses/30/lessons/92342)

시간 초과 코드, 어피치의 사전을 구성하고, Ryan의 사전을 가능한 경우의 수에 따라 계산하는 방식인데  
중간에 백트래킹이나 특정 부분이 잘못 구현된 것으로 보임  
파이썬을 사용할 때는 특별히 제한이 없는 한 표준 라이브러리를 활용하자

```python
import copy
import math
from collections import defaultdict
from typing import Sequence, List, Mapping


def solution(n: int, info: Sequence[int]) -> List[int]:
    answer = [-1]
    score_tracking = [-math.inf]
    apeach_score_counter = {}
    for index, value in enumerate(info):
        apeach_score_counter[10 - index] = value

    def calculate_scores(ryan_score_counter: Mapping[int, int]):
        _apeach_score = 0
        _ryan_score = 0
        for i in range(1, 10 + 1):
            if ryan_score_counter[i] > apeach_score_counter[i]:
                _ryan_score += i
            elif ryan_score_counter[i] < apeach_score_counter[i]:
                _apeach_score += i
            elif (
                ryan_score_counter[i] == apeach_score_counter[i]
                and ryan_score_counter[i] != 0
            ):
                _apeach_score += i
            else:
                continue

        return _apeach_score, _ryan_score

    def search(num_shoot: int, ryan_score_counter: Mapping[int, int]):
        if num_shoot == n:
            # 어피치, 라이언 점수 계산
            # 라이언이 이기면서 이점 점수 차보다 크거나 같으면 저장
            apeach_score, ryan_score = calculate_scores(ryan_score_counter)
            if ryan_score > apeach_score:
                if ryan_score - apeach_score > score_tracking[0]:
                    score_tracking[0] = ryan_score - apeach_score
                    answer[0] = copy.deepcopy(ryan_score_counter)
                elif ryan_score - apeach_score == score_tracking[0]:
                    for i in range(11):
                        if ryan_score_counter[i] > apeach_score_counter[i]:
                            answer[0] = copy.deepcopy(ryan_score_counter)
                            break
            return

        for score in range(10, -1, -1):
            apeach_score, ryan_score = calculate_scores(ryan_score_counter)

            if (
                ryan_score > apeach_score
                and ryan_score_counter[score] > apeach_score_counter[score]
            ):
                continue

            ryan_score_counter[score] += 1
            if answer[0] != ryan_score_counter:
                search(num_shoot + 1, ryan_score_counter)
            ryan_score_counter[score] -= 1

    search(0, defaultdict(int))
    decision = answer[0]
    if decision == -1:
        return [-1]
    else:
        output = []
        for score in range(10, -1, -1):
            output.append(decision[score])
        return output
```

표준 라이브러리를 사용한 더 간결한 풀이
```python
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from typing import Sequence, List, Mapping


def solution(n: int, info: Sequence[int]) -> List[int]:
    def calculate_scores(ryan_score_counter: Mapping[int, int]):
        _apeach_score, _ryan_score = 0, 0
        for score in range(11):
            if ryan_score_counter[score] > apeach_score_counter[score]:
                _ryan_score += score
            elif apeach_score_counter[score] > 0:
                _apeach_score += score
        return _ryan_score, _apeach_score

    def convert_to_list(counter: Mapping[int, int]) -> List[int]:
        result = []
        for score in range(10, -1, -1):
            result.append(counter[score])
        return result

    apeach_score_counter = Counter()
    for index, value in enumerate(info):
        apeach_score_counter[10 - index] = value

    max_diff = 0
    answer = defaultdict(int)
    for combination in combinations_with_replacement(range(11), n):
        current_score_counter = Counter(combination)
        ryan_score, apeach_score = calculate_scores(current_score_counter)

        if ryan_score - apeach_score > max_diff:
            max_diff = ryan_score - apeach_score
            answer = current_score_counter

    return [-1] if not answer else convert_to_list(answer)


assert solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [
    0,
    2,
    2,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
]
assert solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1]
assert solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]) == [
    1,
    1,
    2,
    0,
    1,
    2,
    2,
    0,
    0,
    0,
    0,
]
assert solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]) == [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    2,
]
```

#### [외벽 점검](https://school.programmers.co.kr/learn/courses/30/lessons/60062)

weak 자료구조를 확장해서 시계, 반시계를 시계만 고려하게 문제 조건을 완화하고,
담당할 수 있는 친구를 어떻게 경우의 수 처리를 할 지 (순열)를 캐치해야 풀 수 있는 문제  
구현 난이도도 사실 쉽지는 않다, 커버 불가능하면 인덱스 연산을 갱신하는 부분 등

```python
import math
from itertools import permutations
from typing import List


def solution(n: int, weak: List[int], dist: List[int]) -> int:
    num_of_weak_points = len(weak)

    weak.extend([x + n for x in weak])

    answer = math.inf
    # 1, 5, 6, 10, 13, 17, 18, 22
    # 1, 5, 6, 10
    # 5, 6, 10, 13
    # 6, 10, 13, 17
    # 10, 13, 17, 18
    for i in range(num_of_weak_points):
        for friend_order in permutations(dist):
            friend_count = 1
            position = weak[i] + friend_order[friend_count - 1]

            for j in range(i, i + num_of_weak_points):
                if position < weak[j]:
                    friend_count += 1
                    if friend_count > len(dist):
                        break
                    position = weak[j] + friend_order[friend_count - 1]

            answer = min(answer, friend_count)

    return answer if answer <= len(dist) else - 1


assert solution(12, [1, 5, 6, 10], [1, 2, 3, 4]) == 2
assert solution(12, [1, 3, 4, 9, 10], [3, 5, 7]) == 1
```

#### [사라지는 발판](https://school.programmers.co.kr/learn/courses/30/lessons/92345)

프로그래머스 풀이가 더 직관적이어서 링크로 대체, 추후에 다시 풀어볼 것

- https://school.programmers.co.kr/questions/38680
