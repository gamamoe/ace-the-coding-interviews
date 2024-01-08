import sys; input = sys.stdin.readline
N, M = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(M)]
basket = [a for a in range(0, N+1)]
# 인덱스 활용을 위해 0번부터 각 번호 삽입한 리스트 생성

for ball in lis: # reversed함수로 뒤집은 후, 해당 내용 반영
    # reversed함수에 대해 유념하자
    basket[ball[0] : ball[1] + 1] = reversed(basket[ball[0] : ball[1] + 1])
print(' '.join(map(str, basket[1:])))
# 0번 인덱스 제외하는 효율적인 join 출력