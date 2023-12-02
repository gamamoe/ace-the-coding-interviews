import sys; input = sys.stdin.readline
N = int(input())
lis = list(map(int, input().split()))
print(min(lis), max(lis))
# 정렬해서 양끝을 출력할수도 있지만 여기선 max, min이 O(N)으로 더 효율적
# 정렬을 쓰는 순간 O(N log N)
