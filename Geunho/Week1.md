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