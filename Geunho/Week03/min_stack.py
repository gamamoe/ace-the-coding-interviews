# 155. Min Stack (Easy)
# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        min_val = min(self.getMin(), val) if self._stack else val
        self._stack.append((val, min_val))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]
