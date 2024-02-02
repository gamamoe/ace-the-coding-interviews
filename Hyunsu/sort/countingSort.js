const assert = require("assert");

/**
 * 몸풀기 문제 : 계수 정렬 구현 하기
 * Time Complexity : O(s.length + 26)
 * @param {*} s
 */
function countingSort(s) {
  // 빈도 테이블 생성
  const freq = new Array(26).fill(0);

  // 빈도 테이블 매핑
  s.split("").map((s) => (freq[s.charCodeAt() - 97] += 1));
  console.log(freq);

  // 빈도 테이블을 순회하면서 빈도 수 만큼 문자열 생성
  let result = "";
  freq.forEach((count, i) => {
    result += String.fromCharCode(97 + i).repeat(count);
  });

  return result;
}

assert.equal(countingSort("hello"), "ehllo");
assert.equal(countingSort("algorithm"), "aghilmort");
