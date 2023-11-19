## 프로그래머스 추가 문제

### 평행

```python
def solution(dots):
    p1, p2, p3, p4 = dots

    case1 = (p1[1] - p2[1]) / (p1[0] - p2[0]) == (p3[1] - p4[1]) / (p3[0] - p4[0])
    case2 = (p1[1] - p3[1]) / (p1[0] - p3[0]) == (p2[1] - p4[1]) / (p2[0] - p4[0])
    case3 = (p1[1] - p4[1]) / (p1[0] - p4[0]) == (p2[1] - p3[1]) / (p2[0] - p3[0])

    answer = 1 if any([case1, case2, case3]) else 0
    return answer
```

### 로그인 성공?

- Walrus 연산자를 활용하면 좀 더 간결하게 작성 가능할 듯

```python
from typing import List


def solution(id_pw: List[str], db: List[List[str]]):
    user_id, user_password = id_pw

    user_dict = {}
    for entry in db:
        user_dict[entry[0]] = entry[1]

    if user_id in user_dict:
        if user_password == user_dict[user_id]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
```

### 다음에 올 숫자

등차 또는 등비수열이 보장되므로 공차나 공비 조건 확인 후 마지막 원소에 적절히 처리

```python
from typing import List


def solution(common: List[int]) -> int:
    e1, e2, e3, *_ = common

    if e2 - e1 == e3 - e2:
        return common[-1] + (e2 - e1)
    else:
        return common[-1] * (e2 / e1)
```

### 최빈값 구하기

Counter 자료구조를 활용하면 쉽게 풀 수 있다. 입력 array의 모든 값이 동일한 경우 예외 처리 필요

```python
import collections
from typing import List


def solution(array: List[int]) -> int:
    counter = collections.Counter(array)

    most_common_elements = counter.most_common(2)
    if len(most_common_elements) == 1:
        return most_common_elements[0][0]
    else:
        most_common_element, next_common_element = most_common_elements

        if most_common_element[1] == next_common_element[1]:
            return -1
        else:
            return most_common_element[0]
```