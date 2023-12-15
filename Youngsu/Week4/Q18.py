
# 값이 많아지면 비효율 적 O(N^2)
# def solution(arr, target):
#     answer = False
#     for v in arr:
#         if (target - v in arr) and (target % v != 0):
#             answer = True
#     return answer

def solution(arr, target):
    answer = False
    # 해시테이블 생성
    hashtable = [0] * (max(arr) + 1)
    print(hashtable)
    for v in arr:
        hashtable[v] = 1
    # 타겟을 만드는 쌍 있나 확인
    for v in arr:
        if hashtable[target - v] and (target % v != 0):
            answer = True
            break
    return answer

print(solution([1,2,3,4,8], 6))
print(solution([2,3,5,9], 10))