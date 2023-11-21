def solution(N, stages):
    stages.sort()
    count = []
    for i in range(1, N+1):
        count.append(stages.count(i))
    fail = []
    total = len(stages)
    for j in range(len(count)):
        if j == 0 and total != 0:
            fail.append(count[j]/total)
        elif total != 0 and j > 0:
            total -= count[j-1]
            if total != 0:
                fail.append(count[j]/total)
            else:
                fail.append(0)  # 0에대한 예외처리 필수!
        else:
            fail.append(0)  # 0에대한 예외처리 필수!
    ndict = {key + 1 : value for key, value in enumerate(fail)}
    answer = list(sorted(ndict, key=ndict.get, reverse=True))
    return answer

def solution1(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer


print(solution(2, [1,1,1,1]))