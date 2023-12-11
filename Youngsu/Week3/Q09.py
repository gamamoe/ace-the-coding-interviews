# 10진수를 2진수로 변환하기

def solution(decimal):
    stack = []
    minus = 1
    if decimal < 0:
        minus = -1
        decimal *= -1

    if decimal == 0:
        return 0
    elif decimal == 1:
        return minus * 1

    while decimal > 1:
        stack.append(str(decimal % 2))
        decimal = decimal //2
    stack.append("1")

    binary = minus * int("".join(stack[::-1]))
    return binary

print(solution(10))
print(solution(27))
print(solution(12345))
print(solution(0))
print(solution(-1))
print(solution(-12345))