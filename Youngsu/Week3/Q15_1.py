import time
from collections import deque

def solution(N, K):
    start = time.time()
    queue = deque(range(1, N+1))
    print(queue)
    while len(queue) > 1:
        for _ in range(K - 1):
            queue.append(queue.popleft())
            queue.popleft()
    end = time.time()
    print(f'time = {end - start}')
    return queue[0]

print(solution(1000, 2))