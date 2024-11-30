from collections import deque


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        prev_words = sentence.split()
        next_words = deque(prev_words)
        next_words.rotate(-1)

        for prev_word, next_word in zip(prev_words, next_words):
            if prev_word[-1] != next_word[0]:
                return False

        return True


s = Solution()
assert s.isCircularSentence('leetcode exercises sound delightful')
assert s.isCircularSentence('eetcode')
assert not s.isCircularSentence('Leetcode is cool')
