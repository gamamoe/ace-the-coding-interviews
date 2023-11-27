def solution(arr):
    return sorted(arr)

#def solution(arr):  sort 버전
#    arr.sort()
#    return arr

#def solution(arr):
#    return arr.sort()   이건 작동 안됨. sort()는 정렬하지만 return요구시 None을 반환함!
#

#  sorted(리스트)          <-> list_name.sort()
# 원본은 유지하면서 새로 정렬 <-> 원본을 바꾸고 싶을 때
arr1 = [1,-5,2,4,3]
arr2 = [2,1,1,3,2,5,4]
arr3 = [6,1,7]


def check():
    if solution(arr1) == [-5,1,2,3,4]:
        print(True)
    else:
        print(False)
    if solution(arr2) == [1,1,2,2,3,4,5]:
        print(True)
    else:
        print(False)
    if solution(arr3) == [1,6,7]:
        print(True)
    else:
        print(False)


check()
