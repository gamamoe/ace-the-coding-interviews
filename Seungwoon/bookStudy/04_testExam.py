def solution(answers):
    l1 = [1, 2, 3, 4, 5] * len(answers) # 부족하지않게끔 길이 늘림
    l2 = [2,1,2,3,2,4,2,5] * len(answers)
    l3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    count = [0, 0, 0] # 점수 계산
    for i in range(len(answers)):
        if l1[i] == answers[i]:
            count[0] += 1
        if l2[i] == answers[i]:
            count[1] += 1
        if l3[i] == answers[i]:
            count[2] += 1
    result = []
    max_score = max(count)   # 미리 최댓값 계산
    for idx, v in enumerate(count):
        if max_score == v: # 최댓값과 같으면
            result.append(idx + 1) # 해당 인덱스 추가

    return result