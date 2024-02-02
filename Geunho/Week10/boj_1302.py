import sys
from collections import Counter

num_of_books = int(sys.stdin.readline())
counter = Counter()
for _ in range(num_of_books):
    title = sys.stdin.readline().rstrip()
    counter[title] += 1

sorted_list = sorted(counter.keys(), key=lambda e: (-counter[e], e))
print(sorted_list[0])
