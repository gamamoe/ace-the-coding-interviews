# 같은 알파벳 짝지어서 제거하기

def solution(s):
    stack = []
    for c in s:
        if stack == []:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if stack:
        return 0
    else:
        return 1

print(solution('baabaa'))
print(solution('baba'))