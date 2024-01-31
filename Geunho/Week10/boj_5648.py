# https://www.acmicpc.net/problem/5648
import sys

answer = []
while line := sys.stdin.readline():
    elements = [int(x[::-1]) for x in line.split()]
    if answer:
        answer.extend(elements)
    else:
        answer.extend(elements[1:])

answer.sort()
print("\n".join([str(x) for x in answer]))
