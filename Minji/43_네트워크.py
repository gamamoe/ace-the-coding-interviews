def solution(n, computers):
  visited = [False] * n
  net = 0 # 네트워크 개수
  
  for i in range(n):
    if not visited[i]:
      dfs(computers, visited, i)
      net += 1
      
  return net

def dfs(computers, visited, cur):
  visited[cur] = True

  for next_node, connected in enumerate(computers[cur]):
    if connected and not visited[next_node]:
      dfs(computers, visited, next_node)

assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1