import sys; input = sys.stdin.readline
N, M = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(M)]
# 내용을 2차원 배열로 받은다음

basket = [0] * (N+1) # 바구니 리스트 생성. 인덱스 0은 버리는 개념
for ball in lis: # lis의 한개의 list = ball
    for loc in range(ball[0], ball[1]+1):
        basket[loc] = ball[2] # i부터 j까지 인덱스 위치 값을 ball[2]로 갱신
print(' '.join(str(basket[b]) for b in range(1, len(basket))))
# 띄어쓰기 문자열 공백으로 출력