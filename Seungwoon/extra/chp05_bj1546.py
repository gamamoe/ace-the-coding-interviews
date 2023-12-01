import sys; input = sys.stdin.readline
N = int(input())
lis = list(map(int, input().split()))
print(sum(lis) / max(lis) * 100/N)
# 왜 브론지 1인지 모르겠는 문제