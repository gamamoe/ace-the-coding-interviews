import sys

chunk = sys.stdin.readline().rstrip()
answer = 0
if (str_len := len(chunk)) == 4:
    answer = int(chunk[:2]) + int(chunk[2:])
elif str_len == 3:
    if chunk[1] == "0":
        answer = 10 + int(chunk[2])
    else:
        answer = int(chunk[0]) + 10
else:
    answer = int(chunk[0]) + int(chunk[1])

print(answer)
