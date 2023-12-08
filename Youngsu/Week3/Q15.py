import time
def solution(n, k):
    start = time.time()
    answer = 0
    position = 0
    queue = [i + 1 for i in range(n)]
    while len(queue) > 1:
        position += k - 1
        position %= len(queue)

        queue.pop(position)
    answer = queue[0]
    end = time.time()
    print(f'time = {end - start}')
    return answer

print(solution(1000,2))