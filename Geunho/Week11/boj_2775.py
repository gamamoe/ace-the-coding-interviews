import sys

cache = [[x for x in range(1, 15)]]
for i in range(1, 15):
    entry = []
    for j in range(1, 15):
        entry.append(sum(cache[i - 1][:j]))
    cache.append(entry)

num_of_test_cases = int(sys.stdin.readline())
answer = []
for _ in range(num_of_test_cases):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    answer.append(cache[k][n - 1])

print("\n".join([str(x) for x in answer]))
