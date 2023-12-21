const assert = require("assert");

/**
 * 이 문제의 포인트는
 * [1 2] [3 4] [5 6] [7 8]
 * [1] [2] [3] [4]
 * [1] [2]
 *
 * 주어진 차례에서 2로 나누어 떨어지는 값을 통해 다음 대진 순서가 된다.
 *
 * @param {*} n
 * @param {*} a
 * @param {*} b
 * @returns
 */
function solution(n, a, b) {
  let cnt = 0;
  // 올림을 사용하여 2로 나누어 떨어지는 값을 만든다. a 와 b가 같을 때까지
  while (a !== b) {
    a = Math.ceil(a / 2); //round도 상관없음
    b = Math.ceil(b / 2);
    cnt += 1;
  }
  return cnt;
}

assert.equal(solution(8, 4, 7), 3);
assert.equal(solution(10, 1, 10), 3);
assert.equal(solution(4, 2, 3), 2);
assert.equal(solution(2, 1, 2), 1);
