import sys


def get_next_value(value: int) -> int:
    if value % 2 == 0:
        return value // 2
    else:
        return 3 * value + 1


index = 2
current_value = int(sys.stdin.readline())

if current_value == 1:
    answer = 1
else:
    while (next_value := get_next_value(current_value)) != 1:
        current_value = next_value
        index += 1
    answer = index

print(answer)
