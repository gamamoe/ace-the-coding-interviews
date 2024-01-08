# https://www.acmicpc.net/problem/2178
import sys
from collections import deque


def main():
    num_of_rows, num_of_cols = [int(x) for x in sys.stdin.readline().split()]
    graph = []
    for _ in range(num_of_rows):
        row_str = sys.stdin.readline()
        row = []
        for col in range(num_of_cols):
            row.append(row_str[col])
        graph.append(row)

    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}
    while queue:
        row, col, distance = queue.popleft()

        if row == num_of_rows - 1 and col == num_of_cols - 1:
            print(distance)
            break

        for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_row, next_col = row + d_row, col + d_col

            if (
                0 <= next_row < num_of_rows
                and 0 <= next_col < num_of_cols
                and graph[next_row][next_col] == "1"
                and (next_row, next_col) not in visited
            ):
                queue.append((next_row, next_col, distance + 1))
                visited.add((next_row, next_col))


if __name__ == "__main__":
    main()
