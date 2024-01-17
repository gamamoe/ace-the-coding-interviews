from collections import deque

def solution(maps):
  n, m = len(maps), len(maps[0])
  deq = deque([(0, 0)])
  visited = [[0, 0]]
  answer = -1
  
  while deq:
    loc = deq.popleft()
    
    for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
      row = loc[0] + x
      col = loc[1] + y
      
      # 이동한 위치 범위 안에서 동작
      if row < 0 or row >= n or col < 0 or col >= m:
        continue
      
      # 이동한 위치에 벽(= 0)이 있는 경우
      if maps[row][col] == 0:
        continue
      
      next_loc = [row, col]
      if next_loc not in visited:
        deq.append(next_loc)
        visited.append(next_loc)
  
  return answer

assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1
