# https://www.acmicpc.net/problem/18110
import sys

num_of_thoughts = int(sys.stdin.readline())
difficulties = []
for _ in range(num_of_thoughts):
    difficulty = int(sys.stdin.readline().rstrip())
    difficulties.append(difficulty)

difficulties.sort()
boundary = round((num_of_thoughts * 0.15) + 1e-9)
filtered_difficulties = difficulties[boundary:num_of_thoughts - boundary]

if difficulties:
    average = sum(filtered_difficulties) / len(filtered_difficulties)
    answer = round(average + 1e-9)
else:
    answer = 0

print(answer)
