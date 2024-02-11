from itertools import combinations
import sys


heights = []
for _ in range(9):
    height = int(sys.stdin.readline())
    heights.append(height)

answer = []
for combination in combinations(heights, 7):
    if sum(combination) == 100:
        answer = sorted(combination)
        break

print("\n".join([str(x) for x in answer]))
