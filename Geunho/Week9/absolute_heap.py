# https://www.acmicpc.net/problem/11286
import heapq
import sys

num_of_integers = int(sys.stdin.readline())

integers = []
answer = []
for _ in range(num_of_integers):
    integer = int(sys.stdin.readline())

    if integer:
        heapq.heappush(integers, (abs(integer), integer))
    else:
        if integers:
            _, value = heapq.heappop(integers)
            answer.append(value)
        else:
            answer.append(0)

print("\n".join([str(x) for x in answer]))
