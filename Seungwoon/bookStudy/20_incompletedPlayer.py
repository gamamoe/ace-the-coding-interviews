# 1명빼고 모두 완주. 동명이인 有
# 목적: 그 1명이 누군지 출력
# 해시: dict로 key값 mapping
from collections import defaultdict

def solution(participant, completion):
    dt = defaultdict(int) # value 없을때 기본값을 정함. int, set, list 사용可
    for name in participant: # 이름(key) : 개수(value)
        dt[name] += 1
    for finisher in completion: # 완주자 value 개수 차감
        dt[finisher] -= 1
    for key, val in dt.items(): # value가 0이 아닌 것 출력
        if val > 0:
            return key