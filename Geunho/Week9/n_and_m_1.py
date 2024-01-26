import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
visited = [False] * (n + 1)
sequence = [0] * m


def dfs(pointer: int):
    if pointer == m:
        print(" ".join([str(x) for x in sequence]))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            sequence[pointer] = i
            dfs(pointer + 1)
            visited[i] = False


dfs(0)
