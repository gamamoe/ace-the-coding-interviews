# https://www.acmicpc.net/problem/11931
import sys

num_of_elements = int(sys.stdin.readline())
sequence = []
for _ in range(num_of_elements):
    element = int(sys.stdin.readline())
    sequence.append(element)

sequence.sort()
answer = "\n".join([str(x) for x in sequence])
print(answer)
