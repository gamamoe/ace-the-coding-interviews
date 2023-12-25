import sys

N, M = [int(x) for x in sys.stdin.readline().split()]
password_by_url = {}
for _ in range(N):
    url, password = sys.stdin.readline().split()
    password_by_url[url] = password

answer = []
for _ in range(M):
    url = sys.stdin.readline().strip()
    answer.append(password_by_url[url])

print("\n".join(answer))
