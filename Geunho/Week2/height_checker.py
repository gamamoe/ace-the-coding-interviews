# 1051. Squares of a Sorted Array (Easy)
# https://leetcode.com/problems/height-checker/

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return len([x for x, y in zip(heights, sorted_heights) if x != y])
