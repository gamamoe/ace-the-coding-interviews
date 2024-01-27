from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _in_order(tree_node: Optional[TreeNode]):
            if not tree_node:
                return

            _in_order(tree_node.left)
            answer.append(tree_node.val)
            _in_order(tree_node.right)

        answer = []
        _in_order(root)
        return answer
