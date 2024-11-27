import collections
import sys
from typing import Dict, List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        graph = {idx: [idx + 1] for idx in range(n - 1)}
        graph[n - 1] = []

        answer = []
        for u, v in queries:
            graph[u].append(v)
            answer.append(self._bfs(n, graph))

        return answer

    def _bfs(self, n: int, graph: Dict[int, List[int]]) -> int:
        queue = collections.deque([(0, 0)])
        visited = {0}
        shortest_length = sys.maxsize
        while queue:
            current_node, current_length = queue.popleft()

            if current_node == n - 1:
                shortest_length = min(shortest_length, current_length)

            for adj_node in graph[current_node]:
                if adj_node not in visited:
                    queue.append((adj_node, current_length + 1))
            visited.update(graph[current_node])

        return shortest_length


s = Solution()
assert s.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]) == [3, 2, 1]
assert s.shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]) == [1, 1]
