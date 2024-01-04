const assert = require("assert");
/**
 * 문제에서 요구하는 조건을 하나씩 검사하면서,
 * 룰에 위배 되면, 그 때의 번호와 차례를 반환한다.
 * TimeComplexity: O(n)
 * @param {*} n
 * @param {*} words
 * @returns
 */
function solution(n, words) {
  const wordSet = new Set();
  let answer = [0, 0];
  words.every((word, i) => {
    let isRuleBroken = false;
    wordSet.add(word);
    if (wordSet.size !== i + 1) isRuleBroken = true;
    if (word.length <= 1) isRuleBroken = true;
    let prev = words[i - 1];
    if (prev && prev[prev.length - 1] !== word[0]) isRuleBroken = true;

    if (isRuleBroken) {
      let number = (i + 1) % n === 0 ? n : (i + 1) % n;
      let nth = Math.ceil((i + 1) / n);
      answer = [number, nth];
      return false;
    }
    return true;
  });

  return answer;
}

assert.deepEqual(
  solution(3, [
    "tank",
    "kick",
    "know",
    "wheel",
    "land",
    "dream",
    "mother",
    "robot",
    "tank",
  ]),
  [3, 3]
);
assert.deepEqual(
  solution(5, [
    "hello",
    "observe",
    "effect",
    "take",
    "either",
    "recognize",
    "encourage",
    "ensure",
    "establish",
    "hang",
    "gather",
    "refer",
    "reference",
    "estimate",
    "executive",
  ]),
  [0, 0]
);
assert.deepEqual(
  solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]),
  [1, 3]
);
