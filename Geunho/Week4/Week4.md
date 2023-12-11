### 해시의 개념과 정의



### 문제 풀이

#### 두 개의 수로 특정값 만들기

문제 조건 중 중복되는 원소는 없다는 조건을 체크해야 함. 예를 들어 target이 10이고 element가 5일 때 diff는 5이므로 중복 원소 체크를 안하면 잘못된 결과가 나옴  

```python
from typing import List


def solution(arr: List[int], target: int) -> bool:
    arr_set = set(arr)

    for element in arr:
        diff = target - element
        if diff in arr_set and diff != element:
            return True

    return False


assert solution([1, 2, 3, 4, 8], 6)
assert not solution([2, 3, 5, 9], 10)
```

#### 문자열 해싱을 이용한 검색 함수 만들기

ord 함수는 매번 까먹어서 구글링하는데 기억을 해놓으면 좋을 듯 (아스키 문자에 대응하는 정수값)  
문제 자체는 평이하나 hash 만드는 로직은 면접 때 자주 물어보는 소재 중 하나이므로 기억해두자  
추가로 나머지 연산 시 (a + b) % m == (a % m + b % m) % m도 기억해놓을 것  

```python
from typing import List


# hash(s) = (s[0] + s[1]*p + s[2]*p^2 ... s[n-1]*p^n-1) mod m
# p = 31, m = 1,000,000,007
def hash_func(s: str) -> int:
    p = 31
    m = 1_000_000_007
    hash_val = 0
    for index, char in enumerate(s):
        hash_val += (ord(char) * pow(p, index)) % m

    return hash_val % m


def solution(string_list: List[str], query_list: List[str]) -> List[bool]:
    hash_string_set = {hash_func(s) for s in string_list}

    return [hash_func(s) in hash_string_set for s in query_list]


assert solution(
    ["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]
) == [True, False, False, True]
```

#### 완주하지 못한 선수

동명이인 선수가 있으므로 단순히 set을 변경 후 diff로는 해결되지 않는다  
참가자의 이름: 숫자 counter를 만들고 완주자 명단을 순회하면서 숫자 counter를 줄임  
좀 신박한 풀이로는 participant와 completion을 모두 Counter 객체로 만들고 diff를 구하면 아주 쉽게 풀이 가능

```python
from collections import Counter
from typing import List


def solution(participant: List[str], completion: List[str]) -> str:
    participant_counter = Counter(participant)

    for name in completion:
        participant_counter[name] -= 1
        if participant_counter[name] == 0:
            participant_counter.pop(name)

    answer = []
    for name in participant_counter.keys():
        answer.append(name)

    return answer[0]


assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
assert (
    solution(
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
    )
    == "vinko"
)
assert (
    solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
    == "mislav"
)
```

#### [할인 행사](https://school.programmers.co.kr/learn/courses/30/lessons/131127)

해시 객체를 만들고 날짜별로 슬라이딩하면서 만족하는 지 체크하는 코드  
flag를 이용해서 체크하는 로직이 중복되어있어서 리팩토링이 필요함  
교재의 풀이와 큰 틀에서는 차이가 없는데 이게 O(N)인지는 바로 와닿지는 않음 :(

```python
from collections import Counter
from typing import List


def solution(want: List[str], number: List[int], discount: List[str]) -> int:
    want_num_dict = {}
    for item, num in zip(want, number):
        want_num_dict[item] = num

    counter = Counter(discount[:10])
    flag = True
    for k, v in want_num_dict.items():
        if counter[k] < v:
            flag = False
            break

    answer =  1 if flag else 0
    for i in range(len(discount) - 10):
        counter[discount[i]] -= 1
        counter[discount[i + 10]] += 1

        flag = True
        for k, v in want_num_dict.items():
            if counter[k] < v:
                flag = False
                break

        answer = answer + 1 if flag else answer

    return answer
```