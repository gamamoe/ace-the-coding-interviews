import sys

answer = []
num_of_test_cases = int(sys.stdin.readline())
for _ in range(num_of_test_cases):
    num_of_elements = int(sys.stdin.readline())
    n_tuple = [int(x) for x in sys.stdin.readline().split()]

    current_tuple = n_tuple
    visited = {tuple(current_tuple)}
    while True:
        new_tuple = []
        for first, second in zip(current_tuple, current_tuple[1:] + [current_tuple[0]]):
            new_tuple.append(abs(first - second))

        if new_tuple.count(0) == num_of_elements:
            answer.append("ZERO")
            break
        elif tuple(new_tuple) in visited:
            answer.append("LOOP")
            break
        else:
            visited.add(tuple(new_tuple))
            current_tuple = new_tuple

print("\n".join(answer))
