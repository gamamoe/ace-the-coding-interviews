from collections import defaultdict, deque

connected_nodes_by_node = defaultdict(set)
num_of_nodes = int(input())
for _ in range(num_of_nodes - 1):
    a, b = map(int, input().split())
    connected_nodes_by_node[a].add(b)
    connected_nodes_by_node[b].add(a)

queue = deque([(1, 0)])
parent_node_by_node = {}
while queue:
    node, parent = queue.popleft()
    parent_node_by_node[node] = parent
    connected_nodes = connected_nodes_by_node[node]

    for connected_node in connected_nodes:
        connected_nodes_by_node[connected_node].remove(node)
        queue.append((connected_node, node))


answer = []
for i in range(2, num_of_nodes + 1):
    answer.append(str(parent_node_by_node[i]))
print("\n".join(answer))
