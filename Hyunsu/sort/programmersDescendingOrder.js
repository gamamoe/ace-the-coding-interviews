const assert = require("assert");
function solution(n) {
  return parseInt(
    n
      .toString()
      .split("")
      .sort((a, b) => b - a)
      .join("")
  );
}

// insertion sort 구현

/**
 * insertion sort 구현
 * Time Complexity : O(n^2)
 * 내림 차순 이니 arr[j] 가 arr[j-1] 보다 크면 swap
 * @param {*} n
 */
function insertionSort(n) {
  let arr = n.toString().split("");
  for (let i = 1; i < arr.length; i++) {
    for (let j = i; j > 0; j--) {
      if (arr[j] > arr[j - 1]) {
        [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
      }
    }
  }
  return parseInt(arr.join(""));
}

assert.equal(solution(118372), 873211);
assert.equal(insertionSort(118372), 873211);
