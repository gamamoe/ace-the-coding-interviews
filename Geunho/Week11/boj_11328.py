import sys
from collections import Counter

num_of_test_cases = int(sys.stdin.readline())

answer = []
for _ in range(num_of_test_cases):
    str1, str2 = sys.stdin.readline().split()

    if Counter(str1) == Counter(str2):
        answer.append("Possible")
    else:
        answer.append("Impossible")

print("\n".join(answer))
