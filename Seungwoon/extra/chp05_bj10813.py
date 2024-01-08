import sys; input = sys.stdin.readline
N, M = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(M)]
basket = [a for a in range(0, N+1)]
# 인덱스 활용을 위해 0번부터 각 번호 삽입한 리스트 생성

for ball in lis: # 각 공을 서로 위치 바꾸기(파이썬 형태의 개념!)
    basket[ball[0]], basket[ball[1]] = basket[ball[1]], basket[ball[0]]
print(' '.join(str(basket[ball]) for ball in range(1, len(basket))))