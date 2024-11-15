# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        min_length = min((len(str_) for str_ in strs))

        for i in range(min_length):
            char_set = set((str_[i] for str_ in strs))
            if len(char_set) == 1:
                prefix.append(strs[0][i])
            else:
                break

        return ''.join(prefix)


s = Solution()
assert s.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
assert s.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
