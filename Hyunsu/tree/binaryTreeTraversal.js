const assert = require("assert");

function solution(nums) {
  return [
    preorder(0, nums, []).join(" "),
    inorder(0, nums, []).join(" "),
    postorder(0, nums, []).join(" "),
  ];
}

function preorder(root, nums, result) {
  if (!nums[root]) return;
  result.push(nums[root]);
  preorder(root * 2 + 1, nums, result); //left
  preorder(root * 2 + 2, nums, result);
  return result;
}

function inorder(root, nums, result) {
  if (!nums[root]) return;
  inorder(root * 2 + 1, nums, result);
  result.push(nums[root]);
  inorder(root * 2 + 2, nums, result);
  return result;
}

function postorder(root, nums, result) {
  if (!nums[root]) return;
  postorder(root * 2 + 1, nums, result);
  postorder(root * 2 + 2, nums, result);
  result.push(nums[root]);
  return result;
}

assert.deepEqual(solution([1, 2, 3, 4, 5, 6, 7]), [
  "1 2 4 5 3 6 7",
  "4 2 5 1 6 3 7",
  "4 5 2 6 7 3 1",
]);
