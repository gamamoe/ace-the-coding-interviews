import collections
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        keys = []
        for key, count_ in sorted(counter.most_common(), key=lambda x: x[1]):
            if k == 0:
                break

            if k >= count_:
                k -= count_
                keys.append(key)
            else:
                k = 0

        for key in keys:
            counter.pop(key)

        return len(counter)



s = Solution()
assert s.findLeastNumOfUniqueInts([5, 5, 4], 1) == 1
assert s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2
