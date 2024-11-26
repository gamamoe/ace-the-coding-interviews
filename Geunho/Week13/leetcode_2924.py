from collections import defaultdict
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        in_degree = {node: 0 for node in range(n)}
        for nodes in graph.values():
            for node in nodes:
                in_degree[node] += 1

        answer = []
        for node, degree in in_degree.items():
            if degree == 0:
                answer.append(node)

        return answer[0] if len(answer) == 1 else -1


s = Solution()
assert s.findChampion(3, [[0, 1], [1, 2]]) == 0
assert s.findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1
