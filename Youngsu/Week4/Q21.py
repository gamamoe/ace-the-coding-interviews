def solution(want, number, discount):
    # 1. want와 number를 딕셔너리로 만들고
    # 2. 10일치 목록을 딕셔너리로 만들고
    # 3. 비교하기
    # 4. 다르면, 가장 오래된 날 빼고, 새로운 날 추가 후 비교

    want_dic = dict(zip(want, number))
    discount_dic = {}
    days = 0
    for i, item in enumerate(discount):
        if item not in discount_dic.keys():
            discount_dic[item] = 1
        else:
            discount_dic[item] += 1
        if i >= 10:
            if discount_dic[discount[i - 10]] == 1:
                discount_dic.pop(discount[i - 10])
            else:
                discount_dic[discount[i - 10]] -= 1

        if i >= 10 and discount_dic == want_dic:
            days += 1
    return days

print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice",
                "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

print(solution(["apple"],
               [10],
               ["banana","banana","banana","banana","banana","banana","banana",
                "banana","banana","banana","banana","banana","banana","banana","banana"]))