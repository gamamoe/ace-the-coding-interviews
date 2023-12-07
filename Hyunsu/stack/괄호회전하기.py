from collections import deque

## python에서 dequeue 사용이 쉽고 O(1) 으로 접근이 가능하여 풀어보았습니다.
def solution(s):
    queue = deque(s)
    pair={
        "(":")",
        "[":"]",
        "{":"}"
    }
    answer = 0;
    if len(s)<=1:
        return 0
    for i in range(len(s)):
        if(checkIfBalanced(queue,pair)):
            answer+=1
        queue.append(queue.popleft());
        
    return answer


def checkIfBalanced(copyQueue,pair):
    queue  = copyQueue.copy()
    stack = []
    
    while(len(queue)):
        value = queue.popleft()
        if(pair.get(value)):
            stack.append(value)
            continue
        if(len(stack) and  pair[stack[-1]] == value):
            stack.pop()
            continue
        return False
    
    if len(stack)>0:
        return False
    
    return True


print(solution("[](){}"))