# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    str_A = [str(a) for a in A] # 우선 슬라이싱위해 str로 바꾼걸 str_A로 두고
    key_num = [num[0] + num[-1] for num in str_A] # 각 원소의 양 끝만 남기고 가운데 모두 삭제한걸 key_num
    if len(key_num) == len(set(key_num)):  # 양 끝이 같은게 없으면 바로 -1로 종료
        return -1

    dict = defaultdict(list)
    for i, value in enumerate(key_num):  # key_num에 대해 index(i)와 value로 나열
        dict[value].append(i)

# 이렇게 만들어진 dict는 {key_num의 value값 : 해당 index} 구성입니다.

    index = {key: indices for key, indices in dict.items() if len(indices) > 1}
# 인덱스 리스트 길이가 최소 2개 이상인 것만 추출(1개만 있는건 삭제)

    compare = []  # 후보 리스트 비교 대상
    for k in index.values():  # index 값만 추출한 것에 for문 적용
        if len(k) == 2:  # 양 끝 같은 숫자가 딱 2개뿐이면 2개만 더함
            compare.append(A[k[0]] + A[k[1]])
        elif len(k) >= 3:  # 3개 이상이면 3개중 2개를 뽑아서 더한 것 중 max만 추출
            index_combi = [A[i] for i in k]  # k = [인덱스 리스트] 이므로 A에 해당되는 인덱스만 넣은 리스트 형성
            index_combi.sort() # 오름차순 정렬
            max_sum = index_combi[-1] + index_combi[-2] # 정렬된 것 중 뒤의 것 2개(큰 값 2개)만 선택
            compare.append(max_sum)

    return max(compare)  # 비교 리스트 중 최댓값 추출



A1 = [130, 191, 200, 10] # 140
print(solution(A1))

A2 = [405, 45, 300, 300] # 600
print(solution(A2))

A3 = [50, 222, 49, 52, 25] # -1
print(solution(A3))

A4 = [30, 909, 3190, 99, 3990, 9009] # 9918
print(solution(A4))




