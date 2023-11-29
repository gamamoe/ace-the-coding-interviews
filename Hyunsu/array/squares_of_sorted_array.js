const assert = require("assert");
/**
 * Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 */

/**
 * Simply using map and sort.
 * timeComplexity : O(n) + O(nlogn)-> O(nlogn)
 * @param {*} nums
 * @returns
 */
function solution(nums) {
  return nums.map((num) => num ** 2).sort((a, b) => a - b);
}

/**
 * Using two pointer, the square of number is always positive.
 * The larger number is either left or right.
 * timeComplexity : O(n)
 * @param {*} nums
 */
function solution1(nums) {
  const result = Array(nums.length).fill(0);
  let left = 0,
    right = nums.length - 1;
  let index = nums.length - 1; // 가장 큰 수를 배열의 끝에서부터 채워나가기 위함.

  while (left <= right) {
    if (Math.abs(nums[left]) >= Math.abs(nums[right])) {
      result[index] = nums[left] ** 2;
      left += 1;
    } else {
      result[index] = nums[right] ** 2;
      right -= 1;
    }
    index--;
  }

  return result;
}

assert.deepEqual(solution([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100]);
assert.deepEqual(solution1([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100]);
