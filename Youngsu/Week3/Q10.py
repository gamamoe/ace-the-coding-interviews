# 괄호 회전하기

def is_right(string: str) -> bool:
    stack = []
    pairs = {')':'(' , '}' : '{', ']' : '['}
    for c in string:
        if (c == '(') or (c == '{') or (c == '['):
            stack.append(c)
        else:
            if stack:
                if stack[-1] == pairs[c]:
                    stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
def solution(string: str) -> int:
    right = 0
    if is_right(string):
        right += 1
    list_string = list(string)
    for _ in range(1, len(list_string)):
        temp = list_string.pop(0)
        list_string.append(temp)
        if is_right("".join(list_string)):
            right += 1
    return right

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(}"))
print(solution("}}}"))
