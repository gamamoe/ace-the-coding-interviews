import heapq

def solution(graph, start):
  dist = {node: float("INF") for node in graph}
  dist[start] = 0
  priority_qu = []
  path = {node: [] for node in graph}
  
  heapq.heappush(priority_qu, [dist[start], start])
  
  # 다익스트라 알고리즘 수행
  while priority_qu:
    distance, node = heapq.heappop(priority_qu)
    
    if dist[node] < distance:
        continue
    
    # 이웃 노드를 탐색하고 거리를 업데이트
    for v, w in graph[node].items():
      node_dist = distance + w
      
      # 더 짧은 경로가 발견되면 거리와 경로를 업데이트
      if node_dist < dist[v]:
        dist[v] = node_dist
        heapq.heappush(priority_qu, [node_dist, v])
        path[v] = path[node] + [node]
        
  result = {node: float("INF") for node in graph}
  for node, shortest_path in path.items(): 
    result[node] = shortest_path + [node]
    
  return [dist, result]

assert solution({
	'A': {'B':9, 'C':3},
  'B': {'A':5},
  'C': {'B':1}
}, 'A') == [
	{'A':0, 'B':4, 'C':3},
  {
		'A': ['A'],
    'B': ['A', 'C', 'B'],
    'C': ['A', 'C']
	}
]

assert solution({ \
	'A': {'B':1}, \
  'B': {'C':5}, \
  'C': {'D':1}, \
  'D': {}
}, 'A') == [
	{'A':0, 'B':1, 'C':6, 'D':7}, \
  {
		'A': ['A'], \
    'B': ['A', 'B'], \
    'C': ['A', 'B', 'C'], \
    'D': ['A', 'B', 'C', 'D']
	}
]