### 스택의 개념과 정의

먼저 들어간 것이 마지막에 나오는 LIFO (Last In, First Out 또는 후입선출) 특징을 가지는 자료형   
주요 연산은 push와 pop이 있고, 그 외에 isFull, isEmpty, 그리고 최근에 삽입한 데이터의 위치인 top도 있음   
문제 풀이 때는 **최근에 삽입한 데이터를 대상**으로 뭔가 연산해야 한다면 스택을 떠올리면 좋다  
대부분 스택을 몰라서 못 푸는 것이 아니라 스택을 활용해야 한다는 생각을 못 떠올려서 풀지 못하는 경우가 많으므로  
스택 관련 문제를 많이 풀어보고 스택을 사용해야 한다는 감을 익히는 것이 중요!

### 문제 풀이

#### 괄호 짝 맞추기

전형적인 스택을 활용하는 문제 유형. 다만 조건에서 가장 가까운 (최근) 열린 괄호와 상쇄라는 문구를 키워드로 스택을 떠올려야 함

```python
def solution(s: str) -> bool:
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()

    return False if stack else True


assert solution("(())()")
assert not solution("((())()")
```

#### 10진수를 2진수로 변환하기

마지막 결과값 반환 시 stack pop을 호출하는 것이 조금 더 자연스러운 흐름이긴 함

```python
def solution(decimal: int) -> str:
    stack = []
    while decimal // 2:
        stack.append(decimal % 2)
        decimal //= 2
    stack.append(1)

    return "".join([str(x) for x in stack[::-1]])


assert solution(10) == "1010"
assert solution(27) == "11011"
assert solution(12345) == "11000000111001"
```

#### [괄호 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/76502)

문제 조건인 s의 길이가 1000 이하이므로 O(N^2)로도 풀이 가능  
s가 짧으므로 extended_s 형태로 붙여서 처리했지만, 메모리 제한이 있다면 저자 풀이처럼 모듈러 연산을 통해서 회전을 구현해야 함
닫는 괄호는 짝이 맞지 않으면 flag를 바꾸고 바로 break를 하고 있는 데 다른 사람 풀이처럼 stack에 집어넣으면 불필요한 flag를 없앨 수 있고 마지막에 stack이 비어있는 지 아닌 지로 체크할 수 있어서 더 깔끔함

```python
def solution(s: str) -> int:
    len_of_s = len(s)
    extended_s = f"{s}{s}"
    pair_dict = {")": "(", "]": "[", "}": "{"}

    answer = 0
    for i in range(len_of_s):
        current_s = extended_s[i : len_of_s + i]

        stack = []
        is_valid = True
        for char in current_s:
            if char in {"(", "[", "{"}:
                stack.append(char)
            else:
                if stack:
                    if stack[-1] == pair_dict[char]:
                        stack.pop()
                    else:
                        is_valid = False
                        break
                else:
                    is_valid = False
                    break
    
        answer = answer + 1 if is_valid and not stack else answer

    return answer


assert solution("[") == 0
assert solution("[](){}") == 3
assert solution("}]()[{") == 2
assert solution("[)(]") == 0
assert solution("}}}") == 0
```

#### [짝지어 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12973)

마찬가지로 전형적인 스택 문제, **가장 최근**의 문자가 지금 문자와 같은 지를 체크하는 문제이므로 스택을 떠올려야 함

```python
def solution(s: str) -> int:
    stack = []
    for char in s:
        if stack:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    return 0 if stack else 1


assert solution("baabaa") == 1
assert solution("cdcd") == 0
```

#### [주식 가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)

O(N^2) 풀이, 프로그래머스 기준으로 통과는 가능하나 선형 시간복잡도로 다시 풀어볼 것

```python
from typing import List


def solution(prices: List[int]) -> List[int]:
    answer = []

    num_of_prices = len(prices)
    for i in range(num_of_prices):
        seconds = 0
        for j in range(i + 1, num_of_prices):
            seconds += 1
            if prices[i] > prices[j]:
                break

        answer.append(seconds)

    return answer
```

아래는 O(N) 풀이 방법, 특정 시점에서 가격 하락을 감지하면 앞의 원소들 중 해당 가격보다 큰 값은 한 번에 계산하는 것이 핵심  
이 때 시간상으로 앞의 원소들을 보므로 스택을 떠올릴 수 있어야한다

```python
from typing import List


def solution(prices: List[int]) -> List[int]:
    answer = [0] * len(prices)
    stack = []

    for index, price in enumerate(prices):
        if not stack:
            stack.append(index)
            continue

        while stack and prices[stack[-1]] > price:
            answer[stack[-1]] = index - stack[-1]
            stack.pop()
        stack.append(index)

    for index in stack:
        answer[index] = (len(prices) - 1) - index

    return answer
```

#### [크레인 인형 뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061)

풀이하고 나니 저자의 풀이와 동일한 사고의 흐름이라 짜릿했음 ㅎ  
보드의 열을 각각의 스택으로 관리하고, bucket에서 인접한 동일 인형 index라면 answer 를 2씩 증가시켜주면 된다  
문제 내에서 스택을 써!라는 힌트를 굉장히 많이주는 케이스

```python
from typing import List


def solution(board: List[List[int]], moves: List[int]) -> int:
    n = len(board)
    columns = []
    for i in range(n):
        column = []
        for j in range(n - 1, -1, -1):
            if val := board[j][i]:
                column.append(val)
        columns.append(column)

    stack = []
    answer = 0
    for move in moves:
        target_column = columns[move - 1]
        if not target_column:
            continue

        doll = target_column.pop()
        if stack and stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)

    return answer


assert (
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
    == 4
)
```

#### [표 편집](https://school.programmers.co.kr/learn/courses/30/lessons/81303)

문제 요구 조건대로 구현하여 우선 정확도는 다 통과하는 코드, 효율성은 모두 시간초과남

```python
from typing import List


def solution(n: int, k: int, cmd: List[str]) -> str:
    rows = [x for x in range(n)]
    removed_rows = []
    ptr = k
    for command in cmd:
        command = command.split(" ")

        if command[0] == "U":
            ptr -= int(command[1])
        elif command[0] == "D":
            ptr += int(command[1])
        elif command[0] == "C":
            removed_rows.append(rows[ptr])
            if ptr == len(rows) - 1:
                rows = rows[:ptr]
                ptr -= 1
            else:
                rows = rows[:ptr] + rows[ptr + 1 :]
        else:  # command[0] == "Z"
            row_num = removed_rows.pop()
            if rows[ptr] > row_num:
                ptr += 1

            rows = (
                [x for x in rows if x < row_num]
                + [row_num]
                + [x for x in rows if x > row_num]
            )

    answer = []
    rows = set(rows)
    for i in range(n):
        if i in rows:
            answer.append("O")
        else:
            answer.append("X")
    return "".join(answer)
```

#### [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

순서를 유지해야한다는 말 때문에 덱을 사용했는데, 그냥 arr을 for-loop 순회하면서 조건에 맞으면 append 하면 더 간단하게 풀이 가능

```python
from collections import deque
from typing import List


def solution(arr: List[int]) -> List[int]:
    arr = deque(arr)
    answer = []

    while arr:
        if not answer:
            answer.append(arr.popleft())
            continue

        element = arr.popleft()
        if element == answer[-1]:
            continue
        else:
            answer.append(element)

    return answer


assert solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1]
assert solution([4, 4, 4, 3, 3]) == [4, 3]
```

#### [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

책의 초반 예제와 거의 동일한 문제, 아이디어 그대로 풀면 된다

```python
def solution(s: str) -> bool:
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
            continue

        if char == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(char)

    return False if stack else True
```

#### [컨트롤 제트](https://school.programmers.co.kr/learn/courses/30/lessons/120853)

문제에서 Z가 들어오면 **바로 이전**이라는 힌트를 주므로 스택을 활용해서 풀면 된다  
문제를 잘 읽으면 Z가 제일 처음 나오는 경우는 없으므로 stack이 비어있는 경우는 고려하지 않아도 됨  

```python
def solution(s: str) -> int:
    tokens = s.split(" ")
    stack = []

    for token in tokens:
        if token == "Z":
            stack.pop()
        else:
            stack.append(int(token))

    return sum(stack)
```

### 큐의 개념과 정의

먼저 들어간 것이 먼저 나오는 FIFO (First In, First Out 또는 선입선출) 특징을 가지는 자료형   
주요 연산은 스택과 마찬가지로 push와 pop이 있고, 그 외에 isFull, isEmpty, 그리고 최근에 삽입한 데이터의 위치인 top도 있음   
문제 풀이 때는 발생한 순서대로 처리할 때, 들어오는 이벤트를 처리할 때 등일 때 큐를 떠올리면 좋다   
파이썬에서는 큐를 직접 구현할 필요 없이 deque를 활용하면 됨  

### 문제 풀이

#### 요세푸스 문제

제거할 원소 앞의 원소들을 큐의 뒤쪽에 다시 집어 넣고, 제거를 반복하는 아이디어를 생각하는 게 중요한 문제

```python
from collections import deque


def solution(n: int, k: int) -> int:
    queue = deque([x for x in range(1, n + 1)])

    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        queue.popleft()

    return queue.popleft()


assert solution(5, 2) == 3
```

#### [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)

책의 풀이와는 약간 다르게 풀었음. 항상 첫 번째 원소를 기준으로 배포일을 계산하고  
뒤의 작업들의 진척도를 해당 날짜 기준으로 계산하여 100% 이상이면 배포 카운트를 추가하고, 그만큼 pop하여 다시 첫 번째 원소를 갱신  
큐가 빌 때까지 이 작업을 반복하면 된다

```python
from collections import deque
from math import ceil
from typing import List


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        days = ceil((100 - progresses[0]) / speeds[0])

        num_of_deployments = 0
        for progress, speed in zip(progresses, speeds):
            if progress + days * speed >= 100:
                num_of_deployments += 1
            else:
                break

        for _ in range(num_of_deployments):
            progresses.popleft()
            speeds.popleft()

        answer.append(num_of_deployments)

    return answer


assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
```

#### [카드 뭉치](https://school.programmers.co.kr/learn/courses/30/lessons/159994)

문제 조건에서 순서대로, 그리고 반드시 카드를 써야하며와 같은 문구로 큐를 써야한다는 것만 캐치하면 쉽게 구현 가능한 문제

```python
from collections import deque
from typing import List


def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        current_word = goal[0]

        if cards1 and current_word == cards1[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and current_word == cards2[0]:
            cards2.popleft()
            goal.popleft()
        else:
            return "No"

    return "Yes"


assert (
    solution(
        ["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]
    )
    == "Yes"
)
assert (
    solution(
        ["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]
    )
    == "No"
)
```