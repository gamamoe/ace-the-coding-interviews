def solution(answers):
    pattern_1 = [1,2,3,4,5,]
    pattern_2 = [2,1,2,3,2,4,2,5,]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5,]

    same_count= [0, 0, 0]
    for idx, n in enumerate(answers):
        if pattern_1[idx % len(pattern_1)] == n:
            same_count[0] += 1
        if pattern_2[idx % len(pattern_2)] == n:
            same_count[1] += 1
        if pattern_3[idx % len(pattern_3)] == n:
            same_count[2] += 1

    max_ = max(same_count)
    answer = [idx+1 for idx, s in enumerate(same_count) if s==max_]
    return answer