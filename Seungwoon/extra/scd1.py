# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import combinations

def solution(A):
    B = list(map(str, A)) # 우선 슬라이싱위해 str로 바꾼걸 B로 두고
    sol = [num[0] + num[-1] for num in B] # 각 원소의 양 끝만 남기고 가운데 모두 삭제한걸 sol
    dict = {}  # dict 정의
    for i, value in enumerate(sol):  # sol에 대해 index(i)와 value로 나열
        if value in dict: # sol의 value값이 dict에 key로 있으면
            dict[value].append(i)  # 해당 value(key)값에 i 인덱스 값 추가
        else: # sol의 value값이 dict에 key로 없으면
            dict[value] = [i]  # 그대로 value(key)와 인덱스(i) 값 추가

# 이렇게 만들어진 dict는 {sol의 value값 : 해당 index} 구성입니다.

    index = {key: indices for key, indices in dict.items() if len(indices) > 1}
# 인덱스 리스트 길이가 최소 2개 이상인 것만 추출(1개만 있는건 삭제)

    if len(sol) == len(set(sol)):  # 양 끝이 같은게 없으면 바로 -1로 종료
        return -1

    stick = list(index.values())  # 값만 추출
    compare = []  # 후보 리스트 비교 대상
    for k in stick:
        if len(k) == 2:  # 양 끝 같은 숫자가 딱 2개뿐이면 2개만 더함
            compare.append(A[k[0]] + A[k[1]])
        elif len(k) >= 3:  # 3개 이상이면 3개중 2개를 뽑아서 더한 것 중 max만 추출
            index_combi = list(combinations(k, 2))
            max_sum = max(A[i] + A[j] for i, j in index_combi)
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




