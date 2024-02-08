import sys

num_of_candidates = int(sys.stdin.readline())
candidates = []
for _ in range(num_of_candidates):
    name = sys.stdin.readline().rstrip()
    if len(name) == 3:
        candidates.append(name)

print(sorted(candidates)[0])
