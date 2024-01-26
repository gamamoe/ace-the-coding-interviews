def solution(k, dungeons):
  visited = [False] * len(dungeons)
  
  def explore(k, visited):
    dun_count = 0
    
    for i in range(len(dungeons)):
      if not visited[i] and dungeons[i][0] <= k:
        visited[i] = True
        dun_count = max(dun_count, 1 + explore(k - dungeons[i][1], visited))
        visited[i] = False
    
    return dun_count
  
  return explore(k, visited)

assert solution(80, [[80, 20], [50, 40], [30, 10]]) == 3