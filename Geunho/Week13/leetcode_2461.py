# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
import collections
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums[:k])

        current_sum = sum(nums[:k])
        answer = current_sum if len(counter) == k else 0

        for i in range(1, len(nums) - k + 1):
            left = nums[i - 1]
            right = nums[i + k - 1]

            counter[left] -= 1
            if counter[left] == 0:
                counter.pop(left)
            counter[right] += 1

            current_sum = current_sum + right - left
            if len(counter) == k:
                answer = max(answer, current_sum)

        return answer


s = Solution()
assert s.maximumSubarraySum([14, 7, 7, 7, 12, 7], 2) == 21
assert s.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15
assert s.maximumSubarraySum(nums=[4, 4, 4], k=3) == 0
assert s.maximumSubarraySum(nums=[1], k=1) == 1
assert s.maximumSubarraySum(nums=[1, 1, 1, 7, 8, 9], k=3) == 24
