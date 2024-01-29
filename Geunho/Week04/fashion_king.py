from collections import defaultdict

num_of_test_cases = int(input())
answer = []
for _ in range(num_of_test_cases):
    num_of_clothes = int(input())

    count_by_clothes_type = defaultdict(int)
    for _ in range(num_of_clothes):
        _, clothes_type = input().split(" ")
        count_by_clothes_type[clothes_type] += 1

    num_of_combinations = 1
    for x in count_by_clothes_type.values():
        num_of_combinations *= x + 1
    answer.append(str(num_of_combinations - 1))

print("\n".join(answer))
