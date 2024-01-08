# 차례대로 더하다가 Z 나오면 해당 숫자 빼기 -> 완전 stack 그 자체
# 음수인 경우 - 부호까지 합쳐서 문자열 길이가 길어진다. -> list 변환 필요
def solution1(s):  #stack을 사용하지 않은 풀이
    s = list(s.split()) # 각 원소 list 변환
    answer = 0
    for i, val in enumerate(s): # 인덱스 연산이 필요하면 걍 enumerate 쓰자
        if val != 'Z': # 굳이 stack 구현안해도 조건으로 풀린다.
            answer += int(val)
        else:
            answer -= int(s[i-1])
    return answer



def solution2(s):   #stack을 사용한 풀이
    s = list(s.split()) # 각 원소 list 변환
    answer = [] # 스택 구현 통
    for val in s: # 말 그대로 스택을 하나하나 구현하는 개념
        if val != 'Z':
            answer.append(int(val))
        else:
            answer.pop()
    return sum(answer)