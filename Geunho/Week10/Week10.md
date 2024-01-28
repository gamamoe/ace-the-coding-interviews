### 정렬


### 실전 문제

#### [문자열 내 마음대로 정렬하기](https://school.programmers.co.kr/learn/courses/30/lessons/12915)

문제 조건대로 정렬 비교 함수를 구현하면 쉽게 풀 수 있는 문제  
인덱스 n의 문자가 같은 경우 사전순으로 앞선 문자열이 앞쪽에 위치한다는 부분을 놓치지 말 것

```python
from typing import Sequence, List


def solution(strings: Sequence[str], n: int) -> List[str]:
    return sorted(strings, key=lambda s: (s[n], s))


assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
```

#### [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

우선 입력으로 들어온 n을 string으로 변환 후 내림차순으로 정렬  
정렬된 결과를 join으로 묶어서 string으로 만든 후 최종적으로는 int로 변환해서 반환

```python
def solution(n: int) -> int:
    return int("".join(sorted(str(n), reverse=True)))


assert solution(118372) == 873211
```

#### [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

slicing 연산으로 배열을 잘라내고, 정렬 후 인덱스 결과만 저장하면 쉽게 풀이 가능한 문제  
인덱스 시작이 0이 아니라 1이므로 off-by-one error만 주의

```python
from typing import Sequence, List


def solution(array: Sequence[int], commands: Sequence[Sequence[int]]) -> List[int]:
    answer = []
    for i, j, k in commands:
        sorted_sub_array = sorted(array[i - 1:j])
        answer.append(sorted_sub_array[k - 1])
    return answer
```

#### [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)

문자열을 스택 자료구조를 이용해서 파싱하는 식으로 진행했는데 조금 더 간결하게 작성가능할 것 같다

```python
from collections import deque
from typing import List


def solution(s: str) -> List[int]:
    stack = []
    candidates = []
    temp_container = []
    for token in s[1:-1]:
        if token == "{":
            stack.append(token)
        elif token == "}":
            stack.append("".join(temp_container))
            temp_container.clear()

            queue = deque()
            while (element := stack.pop()) != "{":
                queue.appendleft(int(element))
            candidates.append(set(queue))
        elif token == ",":
            stack.append("".join(temp_container))
            temp_container.clear()
        elif token.isdigit():
            temp_container.append(token)
        else:
            continue

    candidates.sort(key=lambda c: len(c))
    previous_set = candidates[0]
    answer = [min(previous_set)]
    for candidate in candidates[1:]:
        answer.append(min(candidate.difference(previous_set)))
        previous_set = candidate

    return answer


assert solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]
assert solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]
assert solution("{{20,111},{111}}") == [111, 20]
assert solution("{{123}}") == [123]
assert solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]
```

문자열 처리를 이용해서 좀 더 간결하게 풀이한 코드

```python
from typing import List


def solution(s: str) -> List[int]:
    prepared_str = s.lstrip("{").rstrip("}")
    tuple_set = [set(term.split(",")) for term in prepared_str.split("},{")]
    tuple_set.sort(key=lambda _tuple: len(_tuple))

    answer = [min(tuple_set[0])]
    prev = tuple_set[0]
    for x in tuple_set[1:]:
        answer.append(min(x.difference(prev)))
        prev = x

    return [int(x) for x in answer]
```

### 추가 문제

#### [파일명 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/17686)

문제 요구사항대로 구현, TAIL이 빈 문자일 수 있으므로 해당 부분을 주의해야 함

```python
from typing import Sequence, List


def solution(files: Sequence[str]) -> List[str]:
    custom_files = []
    for original_order, file_name in enumerate(files):
        head = []
        index = 0
        while not file_name[index].isdigit():
            head.append(file_name[index])
            index += 1
        head = "".join(head)

        number = []
        while index < len(file_name) and file_name[index].isdigit():
            number.append(file_name[index])
            index += 1
        number = "".join(number)
        tail = file_name[index:]
        custom_files.append((head, number, tail, original_order))

    custom_files.sort(key=lambda file: (file[0].lower(), int(file[1]), file[3]))
    return [f"{head}{number}{tail}" for head, number, tail, _ in custom_files]
```

#### [H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

```python
from collections import Counter
from typing import Sequence


def solution(citations: Sequence[int]) -> int:
    citation_counter = Counter(citations)
    sorted_citations = sorted(citations, reverse=True)

    h_index = {}
    accumulative_sum = 0
    answer = 0
    for citation in sorted_citations:
        if citation in h_index:
            continue

        accumulative_sum += citation_counter[citation]
        h_index[citation] = accumulative_sum

        if citation >= accumulative_sum:
            answer = max(answer, accumulative_sum)

    return answer


assert solution([3, 0, 6, 1, 5]) == 3
assert solution([0, 0, 0, 0, 0]) == 0
assert solution([0, 0, 0, 0, 1]) == 1
assert solution([9, 9, 9, 12]) == 4
```
