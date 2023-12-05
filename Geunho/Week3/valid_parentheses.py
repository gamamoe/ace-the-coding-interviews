# 20. Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in {"(", "[", "{"}:
                stack.append(char)
            else:
                if stack:
                    if parentheses_dict[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return False if stack else True


assert Solution().isValid("()")
assert Solution().isValid("()[]{}")
assert not Solution().isValid("(]")
