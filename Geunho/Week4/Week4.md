### 해시의 개념과 정의

키를 통해서 빠르게 데이터 탐색을 지원하는 자료 구조를 해시라고 한다  
이 때 키를 만들 때 사용하는 함수를 해시 함수라고 하며 다음과 같은 특징이 있다  

- 해시는 단방향으로 동작
- 상수 시간에 바로 찾을 수 있음
- 값을 인덱스로 활용하려면 적절한 변환 과정 필요

위와 같은 특징 중 단방향 동작을 활용한 비밀번호 관리, 상수 시간에 바로 찾을 수 있는 특징을 활용한 데이터베이스 인덱싱 그리고 블록체인에서 활용된다

### 해시 함수

파이썬에서는 딕셔너리 또는 셋 자료형을 통해 상수 시간에 키 검색이 가능하므로 직접 구현할 일은 많지 않다  
그러나 직접 구현한다면 여러 가지 조건들을 고려해야하는 데

1. 해시 함수의 변환 값을 키 (인덱스)로 사용하므로 해시 테이블의 크기를 넘으면 안된다
2. 해시 함수의 변환 값 충돌을 최대한 적게 발생시켜야 한다

실제 구현은 소수와 나눗셈법, 곱셈법 등을 활용하여 만듬

### 충돌 처리

해시 함수의 충돌을 최소한으로 한다고해도 충돌은 언젠가는 발생하게 됨  
아래와 같은 방식으로 충돌을 처리할 수 있다

1. 체이닝을 통한 충돌 처리
2. 오픈 어드레싱을 통한 충돌 처리
3. 이중 해싱을 통한 충돌 처리

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

#### [오픈채팅방](https://school.programmers.co.kr/learn/courses/30/lessons/42888)

문제 설명만 잘 이해하면 쉽게 풀이할 수 있는 문제. user_id는 유니크하고 최종적으로 매핑되는 닉네임만 입력값을 순회하면서 해시테이블에 잘 업데이트하면 된다

```python
from typing import List


def _reformat_log_message(action: str, nickname: str) -> str:
    if action == "Enter":
        return f"{nickname}님이 들어왔습니다."
    else:
        return f"{nickname}님이 나갔습니다."


def solution(record: List[str]) -> List[str]:
    nickname_by_user_id = {}
    logs_to_print = []
    for row in record:
        logs = row.split(" ")
        action = logs[0]

        if action == "Enter":
            user_id, nickname = logs[1], logs[2]
            nickname_by_user_id[user_id] = nickname
            logs_to_print.append((action, user_id))
        elif action == "Leave":
            user_id = logs[1]
            logs_to_print.append((action, user_id))
        else:  # Change
            user_id, nickname = logs[1], logs[2]
            nickname_by_user_id[user_id] = nickname

    answer = []
    for action, user_id in logs_to_print:
        log_message = _reformat_log_message(action, nickname_by_user_id[user_id])
        answer.append(log_message)

    return answer
```

#### [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

각 장르별 총 재생 횟수에 대한 정보와 각 장르에 속한 음원을 요구조건에 맞춰서 정렬 후 상위 2개만 뽑아내는 작업을 구현하면 쉽게 풀 수 있는 문제

```python
from collections import defaultdict
from typing import List


def solution(genres: List[str], plays: List[int]) -> List[int]:
    play_by_genre = defaultdict(int)
    statistic_by_genre = defaultdict(list)

    for index, (genre, play) in enumerate(zip(genres, plays)):
        play_by_genre[genre] += play
        statistic_by_genre[genre].append((play, index))

    sorted_genres = sorted(
        play_by_genre.keys(), key=lambda x: play_by_genre[x], reverse=True
    )

    answer = []
    for genre in sorted_genres:
        play_index_list = statistic_by_genre[genre]
        sorted_play_index_list = sorted(play_index_list, key=lambda x: (-x[0], x[1]))
        answer.extend([x[1] for x in sorted_play_index_list][:2])

    return answer


assert solution(
    ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
) == [4, 1, 3, 0]
```

#### [신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

답안에 필요한 결과를 만들기 위해서 어떤 자료구조 (set, dict)를 사용할 지 잘 고려 하면 어렵지 않게 풀 수 있다  
손으로 그려보는 게 중요한 것 같고, 조금 마음에 안드는 부분은 num_of_blocked_users를 구하는 부분인데 여기를 개선할 수 있으면 좋을 것 같음

```python
from collections import defaultdict
from typing import List


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    already_reported_logs = set()
    report_count_by_user_id = defaultdict(int)
    blocked_user_ids_by_user_id = defaultdict(list)
    for log in report:
        reporter, reported = log.split(" ")
        if (reporter, reported) in already_reported_logs:
            continue

        already_reported_logs.add((reporter, reported))
        report_count_by_user_id[reported] += 1
        blocked_user_ids_by_user_id[reporter].append(reported)

    answer = []
    for user_id in id_list:
        num_of_blocked_users = len(
            [
                x
                for x in blocked_user_ids_by_user_id[user_id]
                if report_count_by_user_id[x] >= k
            ]
        )
        answer.append(num_of_blocked_users)

    return answer
```

#### [메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

Counter의 most_common을 사용하면 중간 부분의 max_num 가지고 처리하는 부분을 깔끔하게 해결할 수 있음

```python
from collections import defaultdict
from itertools import combinations
from typing import List


def solution(orders: List[str], course: List[int]) -> List[str]:
    answer = []

    for r in course:
        count_by_course_combinations = defaultdict(int)
        for order in orders:
            for combination in combinations(order, r):
                count_by_course_combinations["".join(sorted(combination))] += 1

        combination_count = count_by_course_combinations.values()
        if not combination_count or max(combination_count) < 2:
            continue

        max_num_of_combinations = max(combination_count)
        answer.extend(
            [
                x
                for x in count_by_course_combinations.keys()
                if count_by_course_combinations[x] == max_num_of_combinations
            ]
        )

    return sorted(answer)


assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) == [
    "AC",
    "ACDE",
    "BCFG",
    "CDE",
]
assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) == [
    "ACD",
    "AD",
    "ADE",
    "CD",
    "XYZ",
]
assert solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"]
```

#### [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)

첫 번째 테스트케이스에서 시간 초과 나는 코드, 조금 더 고민해보고 안되면 힌트를 봐야할 것 같음  
현재 구현은 단순히 요구하는 대로 조합을 계산하면서 캐싱된 값이 있으면 그걸 최대한 활용하게 구현함

```python
from collections import defaultdict
from itertools import combinations
from typing import List


def solution(clothes: List[List[str]]) -> int:
    count_by_clothes_type = defaultdict(int)
    for row in clothes:
        _, clothes_type = row
        count_by_clothes_type[clothes_type] += 1

    answer = sum(count_by_clothes_type.values())
    cache = {(k,): v for k, v in count_by_clothes_type.items()}
    clothes_type = count_by_clothes_type.keys()
    for i in range(2, len(clothes_type) + 1):
        for combination in combinations(clothes_type, i):
            cache_result = cache.get(combination[:-1])
            num_of_combinations = cache_result * count_by_clothes_type[combination[-1]]

            answer += num_of_combinations
            cache[combination] = num_of_combinations

    return answer


assert (
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
    == 5
)
assert (
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
    == 3
)
```

#### [압축](https://school.programmers.co.kr/learn/courses/30/lessons/17684)

한 글자만 남았을 때와, next_word가 마지막 케이스일 때 예외처리 때문에 좀 지저분하게 작성함  
다른 사람 풀이를 보면 좀더 neat하게 작성할 수 있음, 아이디어 자체는 딕셔너리 활용 문제에 가까움

```python
from typing import List


def solution(msg: str) -> List[int]:
    answer = []
    compression_dict = {
        str(char): ord(char) - 64 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
    current_index, last_index = 0, 26

    while current_index < len(msg):
        current_word = msg[current_index]
        if current_index == len(msg) - 1:
            answer.append(compression_dict[current_word])
            break

        for i in range(current_index + 1, len(msg)):
            next_word = f"{current_word}{msg[i]}"

            if next_word in compression_dict:
                if current_index + len(next_word) == len(msg):
                    answer.append(compression_dict[next_word])
                    current_index += len(next_word)
                    break
                else:
                    current_word = next_word
                    continue
            else:
                answer.append(compression_dict[current_word])
                compression_dict[next_word] = last_index + 1
                last_index += 1
                current_index += len(current_word)
                break

    return answer
```

#### [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

프로그래머스 해쉬 추가 문제. 문제 지문과 예시만 잘 읽어보면 어처구니 없을 정도로 쉽게 풀이 가능한 문제  
굳이 조합이니 뭐니 찾을 필요가 없음

```python
from typing import List


def solution(nums: List[int]) -> int:
    possible_num_of_choices = len(nums) // 2
    return min(len(set(nums)), possible_num_of_choices)
```

#### [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)

해쉬 카테고리에 있지만 정렬로 우선 풀이. 풀고 나니 Trie를 써야하는 문제인 것 같기도 함  
다른 풀이로도 한 번 풀어볼 것

```python
from typing import List


def solution(phone_book: List[str]) -> bool:
    sorted_phone_book = sorted(phone_book)
    index = 0

    while index < len(phone_book) - 1:
        if sorted_phone_book[index + 1].startswith(sorted_phone_book[index]):
            return False
        index += 1

    return True


assert not solution(["119", "97674223", "1195524421"])
assert solution(["123", "456", "789"])
assert not solution(["12", "123", "1235", "567", "88"])
```
