# s를 왼쪽으로 전체길이 다 회전시킬때, 바른 괄호문자열의 개수가 result
# 이 문제는 ({[)]} 같은 경우는 0으로 정의한다. 즉, 여닫는 순서가 무조건 대칭이여야한다.
def is_vaild(s):
    stack = []
    # 괄호 짝을 dict로 정의
    brackets = {'(': ')', '[': ']', '{': '}'}
    for k in s:
        if k in brackets:  # key명시안안해도 자동 key값 체크
            stack.append(k)
        else:  # 굳이 따로 value로 안해도 나머지임
# stack이 비었거나 brackets[key]에 해당하는 value가 닫힌 k와 불일치하는 경우
            if not stack or brackets[stack.pop()] != k: #여기서 k는 닫힌괄호
                return False
    return not stack  # 빈 stack = True


def solution(s):
    answer = 0

    for i in range(len(s)):  # 문자열 움직이기
        rotated_s = s[i:] + s[:i] # 슬라이싱으로 rotate 구현!
        if is_vaild(rotated_s):
            answer += 1

    return answer