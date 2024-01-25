import sys

answer = []
while (number := sys.stdin.readline().rstrip()) != "0":
    left, right = 0, len(number) - 1

    is_palindrome = True
    while left < right:
        if number[left] != number[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    answer.append("yes" if is_palindrome else "no")

print("\n".join(answer))
