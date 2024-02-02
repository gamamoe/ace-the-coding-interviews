# https://www.acmicpc.net/problem/2798
import sys
from itertools import combinations

num_of_cards, constraints_of_sum = [int(x) for x in
                                    sys.stdin.readline().split()]
cards = [int(x) for x in sys.stdin.readline().split()]

answer = 0
for combination in combinations(cards, 3):
    if (sum_of_cards := sum(combination)) > constraints_of_sum:
        continue
    else:
        answer = max(answer, sum_of_cards)

print(answer)
