from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index_dict = defaultdict(list)
        t_index_dict = defaultdict(list)
        for index, (c1, c2) in enumerate(zip(s, t)):
            s_index_dict[c1].append(index)
            t_index_dict[c2].append(index)

        return list(s_index_dict.values()) == list(t_index_dict.values())


solution = Solution()
assert solution.isIsomorphic("egg", "add")
assert not solution.isIsomorphic("foo", "bar")
assert solution.isIsomorphic("paper", "title")
assert not solution.isIsomorphic("bbbaaaba", "aaabbbba")
