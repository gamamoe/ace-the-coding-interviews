def solution(N, stages):
    answer = []
    # 각 스테이지별 인원 수 카운트 == 도달하였으나 클리어 하지 못한 인언수 리스트
    stage_people = []   # i번째 인덱스에 i+1 스테이지 인언수
    for i in range(N + 1):
        stage_people.append(stages.count(i + 1))

    # 총인원수 구하기
    sum_people = len(stages)

    # i번째 스테이지에 도달한 플레이어 수 = 총인원수 - 이전스테이지까지 인원수 합
    in_stage = []   # i번째 인덱스에 총 인원수에서 i-1번째 스테이지까지 인원수 뺀거
    for i in range(N):
        if i==0:
            in_stage.append(sum_people)
        else:
            sum_people -= stage_people[i - 1]
            in_stage.append(sum_people)
    print(f"in_stage = {in_stage}")
    # 스테이지별 실패율 구하기 : 튜플
    fail_ratio = []
    for i in range(N):
        if in_stage[i] == 0:
            fail_ratio.append((i + 1, 0))
        else:
            fail_ratio.append((i + 1, stage_people[i] / in_stage[i]))
    print(f"fail_ratio = {fail_ratio}")
    # 실패율로 내림차순 정렬
    sorted_list = sorted(fail_ratio, key = lambda x : -x[1])
    print(f"sorted_list = {sorted_list}")
    answer = [sorted_list[i][0] for i in range(N)]
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))