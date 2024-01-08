def solution(numbers):
    sum_list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_list.append(numbers[i] + numbers[j])
    return sorted(list(set(sum_list)))

arr1 = [2,1,3,4,1]
arr2 = [5,0,2,7]

print(solution(arr1))
print(solution(arr2))
