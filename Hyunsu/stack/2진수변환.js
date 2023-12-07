const assert = require("assert");
/**
 * 재귀 함수를 이용하여 10진수를 2진수로 변환.
 * @param {} decimal
 * @returns
 */
function solution(decimal) {
  function recursion(quot, remainders) {
    if (quot === 0) return remainders;
    let remainder = quot % 2;

    const answer = recursion(Math.floor(quot / 2), remainder + remainders);
    return answer;
  }
  return recursion(decimal, "");
}

assert.equal(solution(10), 1010);
assert.equal(solution(2), 10);

/**
 * 스택을 이용하여 10진수를 2진수로 변환.
 */
function solution1(decimal) {
  let answer = "";
  let stack = [];
  let quot = decimal;
  while (quot > 0) {
    stack.push(quot % 2);
    quot = Math.floor(quot / 2);
  }

  // 0보다 클경우 while문을 나온다.
  // stack을 pop하면서 answer에 붙여준다.
  while (stack.length) {
    answer += stack.pop();
  }
  return answer;
}
assert.equal(solution1(10), 1010);
assert.equal(solution1(2), 10);
