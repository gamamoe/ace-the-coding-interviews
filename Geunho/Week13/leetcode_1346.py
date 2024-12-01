# https://leetcode.com/problems/check-if-n-and-its-double-exist/
from collections import defaultdict
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        indices_by_element = defaultdict(set)
        for index, element in enumerate(arr):
            indices_by_element[element].add(index)

        for index, element in enumerate(arr):
            indices = indices_by_element.get(2 * element, None)

            if indices is None:
                continue

            if element != 0 or (element == 0 and len(indices) > 1):
                return True

        return False


s = Solution()
assert not s.checkIfExist([-2, 0, 10, -19, 4, 6, -8])
assert s.checkIfExist([10, 2, 5, 3])
assert not s.checkIfExist([3, 1, 7, 11])
