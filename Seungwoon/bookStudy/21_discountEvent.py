# 목적: want가 모두 할인可인 회원등록 날짜 총 일수
# numbers = want에 해당하는 수량. -> key = want : value = number 생각
# 제품은 하루에 하나씩만 구매 可 -> 가입기간이 10일 연속 일치해야함.
from collections import defaultdict


def solution(want, number, discount):
    dt = defaultdict(int)  # want : number

    answer = 0
    for key, val in zip(want, number):  # 두 리스트 한번에 dict로 만들기
        dt[key] = val

    for i in range(len(discount) - 9): # 10개씩 이동하는 형태
        temp = defaultdict(int)  # 임시 기준 dict(반드시 여기서 초기화)
        for j in range(i, i + 10):
#            if discount[j] in dt: 이 부분은 defaultdict으로 생략 可
             temp[discount[j]] += 1 # 자동 +1 연산
        if dt == temp: # 어차피 검증은 여기서 한다.
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
