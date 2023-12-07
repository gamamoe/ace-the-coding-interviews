const assert = require("assert");
function solution(s) {
  let strArr = s.split("");
  let stack = [];

  for (let str of strArr) {
    if (str === "(") {
      stack.push(str);
      continue;
    }
    if (stack.length > 0 && stack[stack.length - 1] === "(" && str === ")") {
      stack.pop();
      continue;
    }
    return false;
  }
  return stack.length > 0 ? false : true;
}

assert.equal(solution("()()()"), true);
assert.equal(solution("(()())"), true);
assert.equal(solution("("), false);
assert.equal(solution(")"), false);
assert.equal(solution("(()"), false);
assert.equal(solution("())"), false);
assert.equal(solution(")()"), false);
