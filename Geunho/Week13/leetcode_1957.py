# https://leetcode.com/problems/delete-characters-to-make-fancy-string
from dataclasses import dataclass


@dataclass
class _CharFrequency:
    char: str
    frequency: int


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append(_CharFrequency(char, 1))
                continue

            if stack[-1].char == char:
                if stack[-1].frequency == 2:
                    continue
                else:
                    stack[-1].frequency += 1
            else:
                stack.append(_CharFrequency(char, 1))

        answer = []
        for char_frequency in stack:
            char, frequency = char_frequency.char, char_frequency.frequency
            answer.extend([char for _ in range(frequency)])

        return ''.join(answer)


s = Solution()
assert s.makeFancyString('leeetcode') == 'leetcode'
assert s.makeFancyString('aaabaaaa') == 'aabaa'
assert s.makeFancyString('aab') == 'aab'
