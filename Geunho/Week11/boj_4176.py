import sys

answer = []
while (line := sys.stdin.readline().rstrip()) != "END":
    i = 1
    previous_number = line
    while True:
        next_number = len(previous_number)
        if previous_number == str(next_number):
            answer.append(str(i))
            break

        previous_number = str(next_number)
        i += 1

print("\n".join(answer))
