from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        cols = []
        for row in box:
            rotated_col = []
            for i in range(n - 1, -1, -1):
                cell = row[i]

                if not rotated_col:
                    rotated_col.append(cell)
                    continue

                if cell == '#':
                    num_of_empty = 0
                    while rotated_col and rotated_col[-1] == '.':
                        rotated_col.pop()
                        num_of_empty += 1
                    rotated_col.append(cell)
                    for _ in range(num_of_empty):
                        rotated_col.append('.')
                else:
                    rotated_col.append(cell)
            cols.append(rotated_col)

        answer = []
        for i in range(n - 1, -1, -1):
            row = []
            for j in range(m - 1, -1, -1):
                row.append(cols[j][i])
            answer.append(row)
        return answer


s = Solution()
assert s.rotateTheBox([['*', '#', '*', '.', '.', '.', '#', '.', '*', '.']]) == [
    ['*'],
    ['#'],
    ['*'],
    ['.'],
    ['.'],
    ['.'],
    ['.'],
    ['#'],
    ['*'],
    ['.'],
]
assert s.rotateTheBox([['#', '.', '#']]) == [['.'], ['#'], ['#']]
assert s.rotateTheBox([['#', '.', '*', '.'], ['#', '#', '*', '.']]) == [
    ['#', '.'],
    ['#', '#'],
    ['*', '*'],
    ['.', '.'],
]
assert s.rotateTheBox(
    [
        ['#', '#', '*', '.', '*', '.'],
        ['#', '#', '#', '*', '.', '.'],
        ['#', '#', '#', '.', '#', '.'],
    ]
) == [
    ['.', '#', '#'],
    ['.', '#', '#'],
    ['#', '#', '*'],
    ['#', '*', '.'],
    ['#', '.', '*'],
    ['#', '.', '.'],
]
