import sys; input = sys.stdin.readline
N, X = map(int, input().split())
A = list(map(int, input().split()))
print(' '.join(str(num) for num in A if num < X))
# 기본이 문자열인 input()과 str만 가능한 join개념을 기억하자.