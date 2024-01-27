# 1295. Find Numbers with Even Number of Digits (Easy)
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
from typing import List

# In general, the time complexity of integer to string is Log10(Val)
# e.g., 12345 => Divide 10 repeatedly to convert '12345'
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in nums if len(str(x)) % 2 == 0])
