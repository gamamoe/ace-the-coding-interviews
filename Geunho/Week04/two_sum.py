from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_by_key = defaultdict(list)
        for index, num in enumerate(nums):
            indices_by_key[num].append(index)

        answer = []
        for index, num in enumerate(nums):
            diff = target - num

            if diff == num and len(indices_by_key[num]) == 2:
                answer = indices_by_key[num]
                break

            if diff != num and diff in indices_by_key:
                answer = [index, indices_by_key[diff][0]]
                break

        return answer


solution = Solution()
assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == sorted([0, 1])
assert sorted(solution.twoSum([3, 2, 4], 6)) == sorted([1, 2])
assert sorted(solution.twoSum([3, 3], 6)) == sorted([0, 1])
