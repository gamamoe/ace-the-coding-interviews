import sys

sequence_length = int(sys.stdin.readline())
sequence = {int(x) for x in sys.stdin.readline().split()}
target_number = int(sys.stdin.readline())
answer = 0
checked = set()
for element in sequence:
    if element in checked:
        continue

    diff = target_number - element
    if diff in sequence and diff != element:
        answer += 1
        checked.add(element)
        checked.add(diff)

print(answer)
