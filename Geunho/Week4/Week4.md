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