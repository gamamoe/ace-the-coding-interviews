/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * dfs를 이용하여 left만으로 갔을 때, 최대 level과 right만으로 갔을 때 최대 level을 비교하여, 더 큰 level리턴
 * TimeComplexity: O(N) - 결국 모든 노드를 다 돌아야 한다. 마지막 긴 노드를 찾기 위해서
 * @param {TreeNode} root
 * @return {number}
 */

var maxDepth = function (root) {
  let leftLevel = 0;
  let rightLevel = 0;

  return traverse(root, 0);

  function traverse(current, level) {
    if (!current) return level;

    leftLevel = Math.max(leftLevel, traverse(current.left, level + 1));
    rightLevel = Math.max(rightLevel, traverse(current.right, level + 1));

    return Math.max(leftLevel, rightLevel);
  }
};
