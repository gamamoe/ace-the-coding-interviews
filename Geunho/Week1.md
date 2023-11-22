## 0장. 코딩 테스트를 준비하기 전에

### 타인의 풀이를 보면 사고의 폭을 넓힐 수 있다
더 나은 시간 복잡도 풀이, 또는 언어의 문법을 잘 활용한 간결한 코드 등  
비단 코딩 테스트뿐만 아니라 우리는 다른 사람의 코드를 수업이 보게 될 것이므로 이런 연습을 해두는 것이 좋다

### 시험 보듯 공부하라

연습을 실전처럼, 실전을 연습처럼  
책에서 모의고사를 제공해 주기는 하지만, 조금 더 실전처럼 긴장감을 가지고 연습을 위해서 AtCoder와 같은 플랫폼을 고려해 보자  
탑코더나 코드포스도 있지만, 시간대나 난이도를 고려했을 때 AtCoder가 적합하다고 판단됨  

## 1장. 코딩 테스트 효율적으로 준비하기

### 언어 선택하기

변수 선언, 함수 정의, 컨테이너 자료형 (자료구조), 조건문, 반복문은 대부분의 범용 프로그래밍 언어에서 지원하므로 본인이 가장 자신 있는 언어를 선택  
개인적으로는 지원하고자 하는 직군의 범용 언어로 준비하는 것이 안전하다고 생각한다

- Spring 백엔드 엔지니어 -> Java, Kotlin
- 프론트엔드 엔지니어 -> JavaScript
- 머신러닝 엔지니어 -> Python

회사나 면접관 성향에 따라 다르지만, 팀에서 주로 쓰는 언어에 제한을 두는 경우가 간혹 있음

### 문제 분석 연습하기

다른 좋은 내용들이 많지만, 특히 중요하다고 생각되는 부분이  

- 입력값을 분석하라
- 핵심 키워드를 파악하라

드물지만 아주 작은 입력값이라면 불필요한 자료구조/알고리즘보다 하드 코딩이 가능할 때도 있고  
입력값에 따라서 우리가 사용할 수 있는 알고리즘이 달라질 수 있으므로 이 부분이 중요하다고 생각된다 (대표적으로 TSP와 같은 문제)  
핵심 키워드 역시 문제로부터 힌트를 얻을 수 있으므로 '항상' 문제를 잘 읽는 버릇을 들이자 (e.g., 쌍, 최근 -> Stack 등)

## 2장. 프로그래머스 완벽 활용 가이드

플랫폼 사용 관련 가이드이므로 생략

## 3장. 알고리즘의 효율 분석

시간 복잡도는 입력 크기에 대한 연산 횟수의 상한을 의미하며, 낮으면 낮을 수록 좋음  
빅오 표기법을 기준으로 최고차항만 남겨서 진행  
선형 시간 O(N) 기준으로 최대 연산 횟수를 1,000만 정도로 고려해서 알고리즘 선택 및 후보군 압축 

## 4장. 코딩 테스트 필수 문법

저자의 서술 전제가 파이선 기초서 1권을 완독했다는 가정이므로 중요하다고 생각하는 부분들만 정리함

### 부동소수점 연산

이진표기를 하므로 실제 예상값과 다른 결과가 나올 수 있음  
책에서 제시하는 예제는 0.1을 3번 더하고 0.3을 빼면 사람은 0을 기대하지만 실제로는 그렇지 않음  
예전에는 대충 1e-9처럼 적당히 아주 작은 수를 기준으로 close를 체크했었는데  
sys.float_info.epsilon을 앞으로는 활용하는 것이 좋겠다  
실무에서는 비슷하게 torch.allclose, numpy.allclose 많이 사용  

```python
import sys

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a - b)  # 아주 작은 값, 그러나 0은 아님

if abs(a - b) < sys.float_info.epsilon:
    print("a와 b는 같은 값")
else:
    print("a와 b는 다른 값")
```

### 리스트

아마 뒤에 나올 것 같지만, 마지막 원소가 아닌 인덱싱으로 값 삭제는 매우 비싼 연산이므로 값 삭제가 빈번하다면 다른 자료구조를 고려

### 딕셔너리

검색, 삽입, 삭제는 매우 중요하므로 잘 숙지할 것. Walrus 연산자를 잘 활용하면 좀 더 간결한 코드 작성이 가능하다
```python
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

key = "kiwi"    # kiwi is not in my_dict
if val := my_dict.get(key):
    print(f"값: {val}")  # 다시 my_dict.get(key) 또는 my_dict[key] 를 호출하지 않아도 됨
else:
    print(f"{key}가 딕셔너리에 없음")
```

### 문자열 추가, 삭제

이뮤터블 객체이므로 추가, 삭제 시 매번 새로운 객체가 생성된다  
따라서 + 연산을 여러 번 반복할 것 같다면 join을 사용
```python
# 매번 새로운 객체 생성
string = "He"
string += "llo"

# join 시 한 번만 새로 객체를 만들면 됨
string_list = ["He", "llo"]
result = "".join(string_list)   # Hello
```

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

### [OX퀴즈](https://school.programmers.co.kr/learn/courses/30/lessons/120907)

좀 복잡하게 풀이했는 데, 다른 사람 풀이 + 문제 조건에 공백 문자를 캐치하여 split 후 검증하면 좀 더 깔끔하게 작성 가능 

```python
from typing import List


def solution(quiz: List[str]) -> List[str]:
    answer = []

    for equation in quiz:
        first_operand = []
        second_operand = []

        index = 0
        while (char := equation[index]) != " ":
            first_operand.append(char)
            index += 1

        index += 1
        operator = equation[index]
        index += 2

        while (char := equation[index]) != " ":
            second_operand.append(char)
            index += 1

        index += 3
        expected_result = []
        for char in equation[index:]:
            expected_result.append(char)

        first_operand = int("".join(first_operand))
        second_operand = int("".join(second_operand))
        expected_result = int("".join(expected_result))
        if operator == "+":
            if first_operand + second_operand == expected_result:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if first_operand - second_operand == expected_result:
                answer.append("O")
            else:
                answer.append("X")

    return answer
```

### Private 기출 문제

```python
import collections
from typing import List


def solution(A: List[int]) -> int:
    my_dict = collections.defaultdict(collections.deque)

    for element in A:
        str_element = str(element)
        key = f"{str_element[0]}{str_element[-1]}"

        if val := my_dict.get(key):
            if len(val) == 1:
                if element > val[0]:
                    val.append(element)
                else:
                    val.appendleft(element)
            else:  # len(val) == 2:
                if val[0] < element <= val[1]:
                    val.popleft()
                    val.appendleft(element)
                elif val[1] < element:
                    val.popleft()
                    val.append(element)
                else:
                    continue
        else:
            my_dict[key] = collections.deque([element])

    answer = -1
    for elements in my_dict.values():
        if len(elements) == 1:
            continue

        answer = max(answer, elements[0] + elements[1])

    return answer

A1 = [130, 191, 200, 10]  # 140
print(solution(A1))
A2 = [405, 45, 300, 300]  # 600
print(solution(A2))
A3 = [50, 222, 49, 52, 25]  # -1
print(solution(A3))
A4 = [30, 909, 3190, 99, 3990, 9009]  # 9918
print(solution(A4))
```

### [특이한 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/120880)

다소 아쉬운 풀이 lambda를 잘 활용하면 더 깔끔하게 풀이 가능

```python
from operator import itemgetter
from typing import List


def solution(numlist: List[int], n: int) -> List[int]:
    diff_num_list = [(abs(n - x), -x) for x in numlist]
    sorted_num_list = sorted(diff_num_list, key=itemgetter(0, 1))
    return [-x[1] for x in sorted_num_list]
```

더 나은 코드
```python
from typing import List


def solution(numlist: List[int], n: int) -> List[int]:
    return sorted(numlist, key=lambda x: (abs(n - x), -x))
```

### [안전지대](https://school.programmers.co.kr/learn/courses/30/lessons/120866)

전체 좌표 갯수를 구하고, 지뢰와 지뢰 인접 좌표를 빼서 안전한 좌표를 구하는 문제  
위험 좌표는 지뢰 위치에 따라 겹칠 수 있으므로 set을 통해서 고유 좌표들만 관리하는 것이 중요하며  
인접 좌표 계산 시 board의 가능한 영역을 벗어나지 않는 조건 체크만 잘 하면 된다

```python
from typing import List


def solution(board: List[List[int]]) -> int:
    n = len(board)
    total_num_of_coordinates = n * n
    risky_coordinates = set()

    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                risky_coordinates.add((y, x))

                for dy, dx in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1),
                ]:
                    if 0 <= y + dy < n and 0 <= x + dx < n:
                        risky_coordinates.add((y + dy, x + dx))

    return total_num_of_coordinates - len(risky_coordinates)
```