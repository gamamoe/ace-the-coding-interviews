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