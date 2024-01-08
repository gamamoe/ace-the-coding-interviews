/**
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 * 94. Binary Tree Inorder Traversal
 * Given the root of a binary tree, return the inorder traversal of its nodes' values.
 * Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 */

/******************************************************************* */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const { BST } = require("../utils/bst");

var inorderTraversal = function (root) {
  result = [];
  inorder(root, result);
  return result;

  function inorder(root, result) {
    if (!root) return;
    inorder(root.left);
    result.push(root.val);
    inorder(root.right);
    return result;
  }
};

const arr = [1, null, 2, 3];
const tree = new BST();

arr.forEach((v) => tree.insert(v));

inorderTraversal(tree);
