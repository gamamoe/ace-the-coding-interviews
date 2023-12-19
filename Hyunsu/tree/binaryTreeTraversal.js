const assert = require("assert");

function solution(nums) {
  return [
    preorder(0, nums, []).join(" "),
    inorder(0, nums, []).join(" "),
    postorder(0, nums, []).join(" "),
  ];
}

/**
 *
 * 0부터 시작하는 경우  인덱스 설정시 기존 설정에서 +1로 세팅
 * preorder: 부모가 pre가 된다.
 *
 * @param {*} root
 * @param {*} nums
 * @param {*} result
 * @returns
 */
function preorder(root, nums, result) {
  if (!nums[root]) return;
  result.push(nums[root]);
  preorder(root * 2 + 1, nums, result); //left
  preorder(root * 2 + 2, nums, result);
  return result;
}

/**
 * inorder :부모가 중간이 된다. 왼쪽에서 리턴되어 나온 다음의 순서.
 * @param {*} root
 * @param {*} nums
 * @param {*} result
 * @returns
 */
function inorder(root, nums, result) {
  if (!nums[root]) return;
  inorder(root * 2 + 1, nums, result);
  result.push(nums[root]);
  inorder(root * 2 + 2, nums, result);
  return result;
}

/**
 * postorder: 부모가 마지막이 된다. 오른쪽에서 리턴되어 나온 다음의 순서.
 * @param {*} root
 * @param {*} nums
 * @param {*} result
 * @returns
 */
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
