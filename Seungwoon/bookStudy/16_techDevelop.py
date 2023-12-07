from math import ceil  # 올림 함수
from collections import deque


def solution(progresses, speeds):
    answer = []
    t = deque()
    for i in range(len(progresses)):  # 시간을 deque로 정리해 저장
        # progresses[i] + speeds[i] * x = 100
        t.append(ceil((100 - progresses[i]) / speeds[i]))

    while t:
        yardstick = t.popleft() # 비교 기준 설정
        count = 1 # 기본값 설정

        while t and yardstick >= t[0]: # 뒷작업 마무리시간보다 기준일이 높으면
            t.popleft() # 뒷 작업 popleft
            count += 1 # 개수 증가

        answer.append(count) # 답안 갱신

    return answer