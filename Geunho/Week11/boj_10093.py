import sys


a, b = [int(x) for x in sys.stdin.readline().split()]
if a > b:
    a, b = b, a

if a == b:
    print("0")
else:
    answer = [f"{b - a - 1}", " ".join([str(x) for x in range(a + 1, b)])]
    print("\n".join(answer))
