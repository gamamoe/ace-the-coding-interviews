# 문제는 타겟값이 나올 수 있는지 없는지 유무이다. 해시를 쓰지 않은 답안
def solution1(arr, target):
    for i in arr:
        value = target - i
        if value != i and value >=0 and value <= target and value in arr:
            return True
    return False

assert solution1(arr1:=[1, 2, 3, 4, 8], target1:=6) == True, '출력값1 에러'
assert solution1(arr2:=[2,3,5,9], target2:=10) == False, '출력값2 에러'