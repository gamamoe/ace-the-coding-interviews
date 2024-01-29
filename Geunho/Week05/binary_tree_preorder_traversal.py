from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _pre_order(tree_node: Optional[TreeNode]):
            if not tree_node:
                return

            answer.append(tree_node.val)
            _pre_order(tree_node.left)
            _pre_order(tree_node.right)

        answer = []
        _pre_order(root)
        return answer


solution = Solution()
assert solution.preorderTraversal(root=None) == []
assert solution.preorderTraversal(root=TreeNode(1)) == [1]
assert solution.preorderTraversal(
    root=TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
) == [1, 2, 3]
