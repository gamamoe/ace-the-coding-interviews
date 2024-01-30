# https://www.acmicpc.net/problem/2910
import sys
from collections import Counter

n, c = [int(x) for x in sys.stdin.readline().split()]
sequence = [int(x) for x in sys.stdin.readline().split()]

index_by_number = {}
frequency_by_number = Counter(sequence)
for index, number in enumerate(sequence):
    if number not in index_by_number:
        index_by_number[number] = index

sequence.sort(key=lambda x: (-frequency_by_number[x], index_by_number[x]))
print(" ".join([str(x) for x in sequence]))
