# 485. Max Consecutive Ones (Easy)
# https://leetcode.com/problems/max-consecutive-ones/description/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        num_of_consecutive_ones = 0
        for num in nums:
            if num == 1:
                num_of_consecutive_ones += 1
            else:
                answer = max(answer, num_of_consecutive_ones)
                num_of_consecutive_ones = 0

        return max(answer, num_of_consecutive_ones)
