def solution(s):
    answer = 0
    stack = []
    length = len(s)
    
    for i in range(length):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if stack:
        answer = 0
    else:
        answer = 1
    
    return answer