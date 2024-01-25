import sys
from collections import deque

num_of_commands = int(sys.stdin.readline())
answer = []
queue = deque([])
for _ in range(num_of_commands):
    command_with_args = sys.stdin.readline().split()

    command = command_with_args[0]
    if command == "push_front":
        queue.appendleft(int(command_with_args[1]))
    elif command == "push_back":
        queue.append(int(command_with_args[1]))
    elif command == "pop_front":
        output = queue.popleft() if queue else -1
        answer.append(output)
    elif command == "pop_back":
        output = queue.pop() if queue else -1
        answer.append(output)
    elif command == "size":
        answer.append(len(queue))
    elif command == "empty":
        answer.append(0 if queue else 1)
    elif command == "front":
        output = queue[0] if queue else -1
        answer.append(output)
    elif command == "back":
        output = queue[-1] if queue else -1
        answer.append(output)
    else:
        continue

print("\n".join([str(x) for x in answer]))
