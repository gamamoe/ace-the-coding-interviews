from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _post_order(tree_node: Optional[TreeNode]):
            if not tree_node:
                return

            _post_order(tree_node.left)
            _post_order(tree_node.right)
            answer.append(tree_node.val)

        answer = []
        _post_order(root)
        return answer


# Iterative version 가장 명료한 코드
# https://leetcode.com/problems/binary-tree-postorder-traversal/solutions/527604/python3-pre-in-post-iteratively-summarization/