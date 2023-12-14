const assert = require("assert");

/**
 * hashTable이용한 풀이
 * TimeComplexity: O(n)
 * @param {*} nums
 * @param {*} target
 * @returns
 */
var twoSum = function (nums, target) {
  let hash = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (!hash.has(nums[i])) return hash.set(target - nums[i], i);
    return [hash.get(nums[i]), i];
  }
};

assert.deepEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
assert.deepEqual(twoSum([3, 2, 4], 6), [1, 2]);
assert.deepEqual(twoSum([3, 3], 6), [0, 1]);
