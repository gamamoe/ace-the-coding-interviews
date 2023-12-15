# 해시테이블 굳이 어렵게 만들 필요 없음
# def hash_func(string):
#     # m = 2 * 10**28
#     m = 1000000007
#     hash = 0
#     for i, c in enumerate(string):
#         hash += (ord(c) * 31 ** i) % m
#     hash %= m
#     return hash
#
# def solution(participant, completion):
#     answer = ""
#     # m = 2 * 10 ** 28
#     m = 1000000007
#     hash_table = [0] * m
#     for player in completion:
#         hash_table[hash_func(player)] = 1
#
#     for player in participant:
#         hash_value = hash_table[hash_func(player)]
#         if hash_value == 0:
#             return player
#         else:
#             hash_table[hash_func(player)] -= 1

def solution(participant, completion):
    dict = {}
    for player in completion:
        if player not in dict.keys():
            dict[player] = 1
        else:
            dict[player] += 1
    for player in participant:
        if player in dict.keys():
            if dict[player] != 0:
                dict[player] -= 1
            else:
                return player
        else:
            return player


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                ["marina", "josipa", "nikola", "filipa"]))
print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "mislav", "ana"]))