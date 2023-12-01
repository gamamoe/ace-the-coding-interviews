import sys; input = sys.stdin.readline

N = int(input())
lis = list(map(int, input().split()))
v = int(input())

print(lis.count(v))
#count = 0
#for num in lis:  for문과 count()비교하면 count()가 우수.
#  if num == v: 실패율문제는 for안에 count()들어가서 문제된 것!
#    count += 1
#print(count)