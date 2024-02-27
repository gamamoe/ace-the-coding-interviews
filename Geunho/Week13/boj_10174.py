import sys

num_of_test_cases = int(sys.stdin.readline())
answer = []
for _ in range(num_of_test_cases):
    text = sys.stdin.readline().rstrip("\n").lower()

    left, right = 0, len(text) - 1
    is_valid = True
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
            continue
        else:
            is_valid = False
            break

    answer.append("Yes" if is_valid else "No")

print("\n".join(answer))
