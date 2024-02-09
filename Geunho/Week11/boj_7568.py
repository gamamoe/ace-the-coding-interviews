import sys

num_of_people = int(sys.stdin.readline())
people_list = []
for _ in range(num_of_people):
    weight, height = [int(x) for x in sys.stdin.readline().split()]
    people_list.append((weight, height))

answer = []
for current_weight, current_height in people_list:
    num_counts = 0

    for next_weight, next_height in people_list:
        if current_weight < next_weight and current_height < next_height:
            num_counts += 1
    answer.append(num_counts + 1)

print(" ".join([str(x) for x in answer]))
