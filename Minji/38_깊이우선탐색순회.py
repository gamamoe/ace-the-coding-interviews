def solution(graph, start):
  res = []
  nodes_list = {}
  visited = []
  
  # 인접 리스트 생성
  for node in graph:
    if node[0] not in nodes_list:
      nodes_list[node[0]] = [node[1]]
    else:
      nodes_list[node[0]].append(node[1])
  
  # 깊이 우선 탐색
  def dfs(node):
    if node not in visited:
      visited.append(node)
      res.append(node)
      
      if node in nodes_list:
        for neighbor in nodes_list[node]:
          dfs(neighbor)
  
  dfs(start)
  
  return res

assert solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A') == ['A', 'B', 'C', 'D', 'E']
assert solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A') == ['A', 'B', 'D', 'E', 'F', 'C']