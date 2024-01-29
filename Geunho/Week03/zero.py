import sys

K = int(sys.stdin.readline().strip())
numbers = []
for _ in range(K):
    number = int(sys.stdin.readline().strip())

    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))
