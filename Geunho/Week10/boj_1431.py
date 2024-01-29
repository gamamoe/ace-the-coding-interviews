# https://www.acmicpc.net/problem/1431
import sys

num_of_guitars = int(sys.stdin.readline())
guitars = []
for _ in range(num_of_guitars):
    guitar = sys.stdin.readline().rstrip()

    digits = [int(c) for c in guitar if c.isdigit()]
    sum_of_serial_numbers = sum(digits) if digits else 0
    guitars.append((len(guitar), sum_of_serial_numbers, guitar))

guitars.sort(key=lambda g: (g[0], g[1], g[2]))
print("\n".join([g[2] for g in guitars]))
