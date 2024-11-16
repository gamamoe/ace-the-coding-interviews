# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def _is_consecutive_and_sorted(arr: List[int]) -> bool:
            for idx in range(len(arr) - 1):
                if arr[idx] >= arr[idx + 1] or arr[idx + 1] - arr[idx] != 1:
                    return False

            return True

        answer = []
        subarray = None
        was_satisfied = False
        for i in range(len(nums) - k + 1):
            if subarray is None:
                subarray = nums[i : i + k]

            if subarray and was_satisfied:
                last_element = nums[i + k - 1]
                subarray = subarray[1:] + [last_element]
                if len(subarray) == 1 or subarray[-1] - subarray[-2] == 1:
                    answer.append(subarray[-1])
                else:
                    was_satisfied = False
                    answer.append(-1)
            else:
                subarray = nums[i : i + k]
                if _is_consecutive_and_sorted(subarray):
                    was_satisfied = True
                    answer.append(subarray[-1])
                else:
                    was_satisfied = False
                    answer.append(-1)

        return answer


s = Solution()
assert s.resultsArray([1, 2, 3, 4, 3, 2, 5], k=3) == [3, 4, -1, -1, -1]
assert s.resultsArray([2, 2, 2, 2, 2], k=4) == [-1, -1]
assert s.resultsArray([3, 2, 3, 2, 3, 2], k=2) == [-1, 3, -1, 3, -1]
assert s.resultsArray([1, 4], k=1) == [1, 4]
