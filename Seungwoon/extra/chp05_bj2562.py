import sys; input = sys.stdin.readline
lis = [int(input()) for _ in range(9)]
# 1개값 여러줄에 걸쳐 input 받는 법을 배운 문제
print(max(lis))
print(lis.index(max(lis)) + 1)

