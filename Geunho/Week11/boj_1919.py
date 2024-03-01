import sys
from collections import Counter

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

counter1 = Counter(word1)
counter2 = Counter(word2)

char_set = set(counter1.keys()).union(set(counter2.keys()))
answer = 0
for c in char_set:
    answer += abs(counter1[c] - counter2[c])

print(answer)
