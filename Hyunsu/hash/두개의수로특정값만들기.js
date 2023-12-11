const asserts = require("assert");

/**
 * Time Complexity : O(n)
 * Space Complexity : O(n)
 *
 * @param {*} arr
 * @param {*} target
 * @returns
 */

function solution(arr, target) {
  const mapper = {};
  for (const num of arr) {
    if (num >= target) continue;
    if (mapper[target - num] && mapper[target - num] === num) return true;
    mapper[num] = target - num;
  }

  return false;
}

/**
 * 책의 계수 정렬 사용
 * 저자는 어떤의도에서 계수정렬을 이용한 풀이법을 제시한 걸까? 좀 더 생각해봐야겠다.
 * 개인적으로는 if에 대한 조건문이 더 간결할 수록 좋다고 생각하는데,
 * 계수 정렬로 num을 인덱스로 매핑한 방법이 조건(?)들을 좀 더 생각해야 하는것 같다.
 */

function solution1(arr, target) {
  //계수정렬
  const mapper = countSort(arr, target);

  for (const num of arr) {
    if (num >= target) continue;
    if (num === target - num) continue;
    if (mapper[target - num] && mapper[target - num] === 1) return true;
  }

  return false;
}
// O(n)
function countSort(arr, target) {
  const mapper = [];
  for (const num of arr) {
    if (num < target) {
      mapper[num] = 1;
    }
  }
  return mapper;
}
// asserts.equal(solution([1, 2, 3, 4, 8], 6), true);
// asserts.equal(solution([1, 2, 3, 4, 8], 1), false); //target-num이 음수의 경우
// asserts.equal(solution([1, 10000], 2), false);
// asserts.equal(solution([1, 10000], 10001), true);

// asserts.equal(solution1([1, 2, 3, 4, 8], 6), true);
asserts.equal(solution1([1, 2, 3, 4, 8], 1), false); //target-num이 음수의 경우
// asserts.equal(solution1([1, 10000], 2), false);
// asserts.equal(solution1([1, 10000], 10001), true);
