def solution(A):
    sum = []
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if (str(A[i])[0]==str(A[j])[0]) & (str(A[i])[-1]==str(A[j])[-1]):
                sum.append(A[i]+A[j])
    answer = max(sum) if sum else [-1]
    return answer





A1 = [130, 191, 200, 10] # 140
print(solution(A1))

A2 = [405, 45, 300, 300] # 600
print(solution(A2))

A3 = [50, 222, 49, 52, 25] # -1
print(solution(A3))

A4 = [30, 909, 3190, 99, 3990, 9009] # 9918
print(solution(A4))
