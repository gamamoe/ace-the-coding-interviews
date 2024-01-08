# stack idea: '('가 나오면 append.  ')'가 나오면 pop. 통이 True면(비어있지않으면) False
def solution(s):
    answer = []
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            try:
                answer.pop()
            except:  # pop연산에 에러가 출력될 경우
                return False
    return False if answer else True