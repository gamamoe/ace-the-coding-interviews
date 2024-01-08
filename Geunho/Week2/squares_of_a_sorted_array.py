# 977. Squares of a Sorted Array (Easy)
# https://leetcode.com/problems/squares-of-a-sorted-array/
from collections import deque
from typing import List


class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     return sorted([x * x for x in nums])

    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        positive_nums = deque([x for x in nums if x >= 0])
        negative_nums = deque([x for x in nums if x < 0])

        while positive_nums or negative_nums:
            if positive_nums and not negative_nums:
                val = positive_nums[0] ** 2
                positive_nums.popleft()
                answer.append(val)
            elif not positive_nums and negative_nums:
                val = negative_nums[-1] ** 2
                negative_nums.pop()
                answer.append(val)
            elif positive_nums and negative_nums:
                if positive_nums[0] < -negative_nums[-1]:
                    val = positive_nums[0] ** 2
                    positive_nums.popleft()
                    answer.append(val)
                else:
                    val = negative_nums[-1] ** 2
                    negative_nums.pop()
                    answer.append(val)

        return answer
