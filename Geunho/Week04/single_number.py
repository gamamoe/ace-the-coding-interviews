from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor


assert Solution().singleNumber([2, 2, 1]) == 1
assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
assert Solution().singleNumber([1]) == 1
