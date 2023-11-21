def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr1_col = len(arr1[0])
    arr2_col = len(arr2[0])
    answer = [[0] * arr2_col for _ in range(arr1_row)]
    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(arr1_col):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer

# Example usage
arr1 = [
    [1, 4],
    [3, 2],
    [4, 1]
]
arr2 = [
    [3, 3],
    [3, 3]
]

result = solution(arr1, arr2)
print(result)
