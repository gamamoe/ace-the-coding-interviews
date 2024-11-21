# https://leetcode.com/problems/count-unguarded-cells-in-the-grid
from dataclasses import dataclass
from typing import List, Set


@dataclass(frozen=True)
class Point:
    row: int
    col: int


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        walls_or_guards = {Point(row, col) for row, col in guards + walls}
        visited = set()

        for row, col in guards:
            point = Point(row, col)
            self._search(m, n, point, Point(0, 1), walls_or_guards, visited)
            self._search(m, n, point, Point(0, -1), walls_or_guards, visited)
            self._search(m, n, point, Point(1, 0), walls_or_guards, visited)
            self._search(m, n, point, Point(-1, 0), walls_or_guards, visited)

        return m * n - len(walls_or_guards) - len(visited)

    def _search(
        self,
        m: int,
        n: int,
        point: Point,
        direction: Point,
        walls_or_guards: Set[Point],
        visited: Set[Point],
    ):
        current_row = point.row + direction.row
        current_col = point.col + direction.col
        while 0 <= current_row < m and 0 <= current_col < n:
            current_point = Point(current_row, current_col)
            if current_point in walls_or_guards:
                break

            current_row += direction.row
            current_col += direction.col
            if current_point in visited:
                continue
            visited.add(current_point)


s = Solution()
assert (
    s.countUnguarded(
        m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]
    )
    == 7
)
assert (
    s.countUnguarded(m=3, n=3, guards=[[1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]])
    == 4
)
