from collections import defaultdict

def solution(graph, start):
  nodes_dict = defaultdict(list)
  
  # 인접 리스트 생성
  for n, m in graph:
    nodes_dict[n].append(m)
  
  # 너비 우선 탐색
  return bfs(nodes_dict, start)

def bfs(dicts, node):
  visited = []
  qu = []
  
  for nodes in dicts:
    if nodes == node and node not in visited:
        qu.append(node)
        visited.append(node)
        
        if node in visited: qu.pop()
    
    for n in dicts[nodes]:
      if n not in visited:
        qu.append(n)
        visited.append(n)
        
        if n in visited: qu.pop()
  
  return visited


assert solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1) == [1, 2, 3, 4, 5, 0]