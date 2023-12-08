def solution(arr1, arr2):
    answer = [[]]
    i = len(arr1)
    j = len(arr1[0])
    k = len(arr2[0])
    
    answer = [[0] * k for _ in range(i)]

    for row in range(i):
        for col in range(k):
            for l in range(j):
                answer[row][col] += arr1[row][l] * arr2[l][col]
    return answer

A = [[1,4], [3,2], [4,1]]
B = [[3,3], [3,3]]
print(solution(A, B))