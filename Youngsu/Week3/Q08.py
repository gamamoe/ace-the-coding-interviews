# 소괄호가 정상적으로 열리고 닫혔다면 True, 아니면 False 리턴

def solution(input):
    stack = []
    for c in input:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

print(solution('(())()'))
print(solution('((())()'))
print(solution(')()()()'))



