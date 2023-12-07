from collections import deque
# 순서대로 하나씩 꺼낼 때 goal과 일치 可인지 판별

def why(cards1, cards2, goal): # 왜 이건 안될까?
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        yardstick = goal.popleft()
        if cards1 and cards1[0] == yardstick:
            cards1.popleft()
        elif cards2 and cards2[0] == yardstick:
            cards2.popleft()
        else:
            break

    return "No" if goal else "Yes"



def solution(cards1, cards2, goal): # 책의 풀이와 99% 일치
    cards1 = deque(cards1)  # 리스트를 deque로 바꿀 때 이렇게 정의한다.
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break

    return "No" if goal else "Yes"


# 반례 (테스트25)
print(solution(["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"])) #No