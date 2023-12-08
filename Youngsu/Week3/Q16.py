def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    while n > 0:
        while progresses[0] < 100:
            for i in range(n):
                progresses[i] += speeds[i]
        complete = 0
        for _ in range(n):
            if progresses[0] >= 100:
                complete += 1
                progresses.pop(0)
                speeds.pop(0)
                n -= 1
            else:
                continue
        answer.append(complete)
    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([99, 98], [1, 1]))
# print(solution([90, 90], [10, 9]))
print(solution([90, 90, 90, 90],[30, 1, 1, 1]))