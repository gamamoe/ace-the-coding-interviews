import sys; input = sys.stdin.readline
lis = [int(input()) for _ in range(28)]
total_lis = [num for num in range(1,31)]
for num in lis:
    total_lis.remove(num)
print(total_lis[0])
print(total_lis[1])
# N^2 시간복잡도이지만 길이 28고정이므로 O(N)
