from collections import Counter


def solution(N, stages):
    # 1 ~ N+1 challenger count
    # challenger = [0] * (N+2)
    challenger = Counter()
    for stage in stages:  # O(n)
        challenger[stage] += 1
    print(challenger)

    failure_rate = [0]*N
    total = len(stages)
    for stage in range(1, N+1):  # 1<=N<=500
        if challenger[stage] == 0:
            failure_rate[stage-1] = 0
        else:
            failure_rate[stage-1] = challenger[stage]/total
            total -= challenger[stage]

    result = sorted(range(1, N+1), key=lambda x: failure_rate[x-1], reverse=True)
    return result

# 처음 도전한 솔루션
# 정렬을 사용해서 (nlogn)
# 프로그래머스 테스트 시 2개의 timeout과 1개의 실패가 있었음(24/27)
def solution_backup(N, stages):
    global stage
    TOTAL_USER_COUNT = len(stages)
    failure_rate = [0]*N
    prev_stage, challenger, current_failure = 0, 0, 0
    for i, stage in enumerate(sorted(stages)):  # O(nlogn)
        if prev_stage is not stage:
            if current_failure:
                failure_rate[prev_stage-1] = current_failure/challenger
            current_failure = 1
            challenger = TOTAL_USER_COUNT-i
            prev_stage = stage
        else:
            current_failure += 1
    if stage < N+1:
        failure_rate[stage-1] = current_failure/challenger
    answer = sorted(range(1, N+1), key=lambda x: failure_rate[x-1], reverse=True)
    return answer
