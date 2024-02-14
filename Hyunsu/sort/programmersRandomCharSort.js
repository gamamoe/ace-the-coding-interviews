const assert = require("assert");
function solution(strings, n) {
  //각 문자열의 인덱스 n번째 글자를 기준으로 오름차순
  var answer = [];

  const freq = Array.from({ length: 26 }, () => []);
  strings.map((s) => freq[s[n].charCodeAt() - 97].push(s));

  freq.forEach((arr) => {
    if (!arr.length) return false;
    arr.sort();
    answer.push(...arr);
  });

  return answer;
}

assert.deepEqual(solution(["sun", "bed", "car"], 1), ["car", "bed", "sun"]);
assert.deepEqual(solution(["abce", "abcd", "cdx"], 2), ["abcd", "abce", "cdx"]);
