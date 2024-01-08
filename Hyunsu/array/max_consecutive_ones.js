const assert = require("assert");
/**
 * @param {number[]} nums
 * @return {number}
 * time complexity: O(n)
 */

var findMaxConsecutiveOnes = function (nums) {
  let max = 0;
  let accOne = 0;

  for (const num of nums) {
    if (num) {
      accOne += 1;
      max = Math.max(max, accOne);
    } else {
      accOne = 0;
    }
  }
  return max;
};

assert.equal(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3);
assert.equal(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2);
assert.equal(findMaxConsecutiveOnes([0, 0, 0, 0, 0, 0]), 0);
assert.equal(findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1]), 6);
assert.equal(findMaxConsecutiveOnes([0, 1]), 1);
