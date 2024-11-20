# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
from collections import Counter

# FIXME: 131 / 142 testcases passed
class Solution:
    def _take_left_first(self, s: str, k: int) -> int:
        left, right = 0, len(s) - 1
        counter = Counter({'a': 0, 'b': 0, 'c': 0})
        while left <= right:
            if all((freq >= k for freq in counter.values())):
                break

            left_char = s[left]
            right_char = s[right]

            if counter[left_char] < k:
                counter[left_char] += 1
                left += 1
            elif counter[right_char] < k:
                counter[right_char] += 1
                right -= 1
            else:
                temp_left = left
                while temp_left < right and counter[s[temp_left]] >= k:
                    temp_left += 1

                temp_right = right
                while left < temp_right and counter[s[temp_right]] >= k:
                    temp_right -= 1

                if abs(left - temp_left) <= abs(right - temp_right):
                    while left < temp_left:
                        counter[s[left]] += 1
                        left += 1
                else:
                    while temp_right < right:
                        counter[s[right]] += 1
                        right -= 1

        return sum(counter.values())

    def _take_right_first(self, s: str, k: int) -> int:
        left, right = 0, len(s) - 1
        counter = Counter({'a': 0, 'b': 0, 'c': 0})
        while left <= right:
            if all((freq >= k for freq in counter.values())):
                break

            left_char = s[left]
            right_char = s[right]

            if counter[right_char] < k:
                counter[right_char] += 1
                right -= 1
            elif counter[left_char] < k:
                counter[left_char] += 1
                left += 1
            else:
                temp_left = left
                while temp_left < right and counter[s[temp_left]] >= k:
                    temp_left += 1

                temp_right = right
                while left < temp_right and counter[s[temp_right]] >= k:
                    temp_right -= 1

                if abs(right - temp_right) <= abs(left - temp_left):
                    while temp_right < right:
                        counter[s[right]] += 1
                        right -= 1
                else:
                    while left < temp_left:
                        counter[s[left]] += 1
                        left += 1

        return sum(counter.values())

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        counter = Counter(s)
        if len(counter) < 3 or any((freq < k for freq in counter.values())):
            return -1

        return min(self._take_left_first(s, k), self._take_right_first(s, k))


solution = Solution()
assert solution.takeCharacters('cbbac', 1) == 3
assert solution.takeCharacters('acba', 1) == 3
assert solution.takeCharacters('abc', 1) == 3
assert solution.takeCharacters('aabaaaacaabc', 2) == 8
assert solution.takeCharacters('a', 1) == -1
