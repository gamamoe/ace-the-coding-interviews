class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_set = set()
        while True:
            val = 0
            for char in str(n):
                val += int(char) ** 2

            if val == 1:
                break

            previous_count = len(cycle_set)
            cycle_set.add(val)
            if previous_count == len(cycle_set):
                return False
            else:
                n = val

        return True


assert Solution().isHappy(19)
assert not Solution().isHappy(2)