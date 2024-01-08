import sys; input= sys.stdin.readline
lis = []
for num in range(10):
    lis.append(int(input()) % 42)
# input을 여기에 삽입해서 코드 효율성(?)을 증진한 케이스
print(len(set(lis))) # set으로 중복지우고 len 바로 측정

