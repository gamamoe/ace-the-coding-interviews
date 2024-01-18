from collections import deque

def solution(maps):
  n, m = len(maps), len(maps[0])
  deq = deque([((0, 0), 1)])
  visited = {(0, 0)}
  
  while deq:
    loc, dist = deq.popleft()
    
    for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
      row = loc[0] + x
      col = loc[1] + y
      
      # 이동한 위치 범위 안에서 동작
      if row < 0 or row >= n or col < 0 or col >= m:
        continue
      
      # 이동한 위치에 벽(= 0)이 있는 경우
      if maps[row][col] == 0:
        continue
      
      next_loc = (row, col)
      if next_loc not in visited:
        deq.append((next_loc, dist + 1))
        visited.add(next_loc)
        
        # 도착
        if next_loc == (n - 1, m - 1):
          return dist + 1
        
  # 도착 불가
  return -1

assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1
