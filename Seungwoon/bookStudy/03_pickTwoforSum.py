def solution(numbers):
    numbers.sort()
    answer = []
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):  # i+1 유념!
            answer.append(numbers[i] + numbers[k])
    return list(set(answer))


N1 = [2,1,3,4,1]
N2 = [5,0,2,7]
print(solution(N1))  # [2,3,4,5,6,7]
print(solution(N2))  # [2,5,7,9,12]