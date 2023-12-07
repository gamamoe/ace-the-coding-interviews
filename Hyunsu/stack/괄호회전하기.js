const assert = require("assert");

/**
 * js에서는 dequeue를 지원하지 않으므로, 배열의 마지막에 문자를 추가하고 sliding window를 이용하여 회전 시킵니다.
 * Time Complexity: O(1000000) =
 * 회전시킬 횟수 O(1000) * 올바른 괄호인지 확인 O(1000)
 * @param {*} s
 * @returns
 */
function solution(s) {
  let answer = 0;
  let s_arr = s.split("");
  let x = s.length;
  const pair = {
    "(": ")",
    "[": "]",
    "{": "}",
  };
  let start = 0;

  while (x > 0) {
    //올바른 괄호인지 확인하기

    if (checkIfBalanced(s_arr, start, pair)) {
      answer += 1;
    }
    //괄호 회전하기
    // dequeue 대신 sliding window로 s회전 시키기

    s_arr.push(s_arr[start]);
    start += 1;
    x -= 1;
  }
  return answer;
}

function checkIfBalanced(s_arr, start, pair) {
  let stack = [];

  for (let i = start; i < s_arr.length; i++) {
    if (pair[s_arr[i]]) {
      stack.push(s_arr[i]);
      continue;
    }
    if (stack.length > 0 && pair[stack[stack.length - 1]] === s_arr[i]) {
      stack.pop();
      continue;
    }
    return false;
  }

  if (stack.length !== 0) return false;
  return true;
}

assert.equal(solution("[](){}"), 3);
assert.equal(solution("}]()[{"), 2);
assert.equal(solution("[)(]"), 0);

assert.equal(
  checkIfBalanced(["(", ")", "(", ")"], 0, {
    "(": ")",
    "[": "]",
    "{": "}",
  }),
  true
);
assert.equal(
  checkIfBalanced(["(", ")", "(", "}"], 1, {
    "(": ")",
    "[": "]",
    "{": "}",
  }),
  false
);
assert.equal(
  checkIfBalanced([")", ")"], 0, {
    "(": ")",
    "[": "]",
    "{": "}",
  }),
  false
);
assert.equal(
  checkIfBalanced(["{", "(", ")", "}"], 0, {
    "(": ")",
    "[": "]",
    "{": "}",
  }),
  true
);
