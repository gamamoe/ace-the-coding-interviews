def solution(arr):
    return sorted(list(set(arr)), reverse=True)

arr1 = [4,2,2,1,3,4]
arr2 = [2,1,1,3,2,5,4]

print(solution(arr1))
print(solution(arr2))