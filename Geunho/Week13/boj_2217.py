import sys

num_of_ropes = int(sys.stdin.readline())
ropes = []
for _ in range(num_of_ropes):
    rope = int(sys.stdin.readline())
    ropes.append(rope)

ropes.sort(reverse=True)

answer = 0
for index in range(1, num_of_ropes + 1):
    answer = max(answer, ropes[index - 1] * index)

print(answer)
