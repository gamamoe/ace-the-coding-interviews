import sys


answer = []
for _ in range(3):
    sequence = [int(x) for x in sys.stdin.readline().split()]
    zero_count = sequence.count(0)

    if zero_count == 0:
        answer.append("E")
    elif zero_count == 1:
        answer.append("A")
    elif zero_count == 2:
        answer.append("B")
    elif zero_count == 3:
        answer.append("C")
    elif zero_count == 4:
        answer.append("D")

print("\n".join(answer))
