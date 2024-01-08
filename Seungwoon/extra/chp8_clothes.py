# 매일 다른 옷 조합해서 입기. 종류별 1개만 착용 可. 일부가 겹쳐도 추가되면 다른방법으로 인정
# clothes: 옷 리스트   목표: 서로 다른 옷 조합의 수
# dt = {옷의 종류: 옷 리스트}
# 수학적 아이디어 : 안입는 경우가 각 품목별로 'nude' 가 있다고 가정해야 한다.
# 각 종류별로 1개까지만 착용이 가능하므로 전체길이C1을 종류만큼 곱하는 것이다.
from collections import defaultdict


def solution(clothes):
    dt = defaultdict(list)
    for i in clothes:
        dt[i[1]].append(i[0])

    answer = 1  # 0을 곱하면 안되므로 1로 초기화
    for val in dt.values():
        answer *= len(val) + 1  # 여기서 더해지는 1은 각 카테고리별 nude인 경우 추가하는 것.
    return answer - 1  # 모두 안입는 nude경우 제외