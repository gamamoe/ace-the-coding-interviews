const asserts = require("assert");

function solution(stringList, queryList) {
  const hash = {};
  // O(n) hash 생성
  for (const str of stringList) {
    hash[hashing(str)] = str;
  }

  // queryList를 순회하면서 hash에 존재하는지 확인
  return queryList.map((str) => hash[hashing(str)] === str);
}

/**
 * 1차 시도  : str:  NaN 출력 -> Infinity % 1000000007 = NaN
 * js의 Number.MAX_SAFE_INTEGER는 2^53 - 1 초과
 * overflow
 * @param {*} str
 * @returns
 */
function hashing(str) {
  let result = 0;
  let p = 31,
    m = 1000000007;
  for (let i = 0; i < str.length; i++) {
    result += (str.charCodeAt(i) * Math.pow(p, i)) % m;
  }
  return result % m;
}

/**
 * 2차시도 : overflow 방지 위해 Math.pow에 대한 modular연산 추가
 * @param {*} str
 * @param {*} isModular
 * @returns
 */
function hashing(str, isModular = true) {
  let result = 0;
  let p = 31,
    m = 1000000007,
    pPow = 1;
  for (let i = 0; i < str.length; i++) {
    let a = str.charCodeAt(i) * pPow;
    pPow = (pPow * p) % m;
    result += a % m;
  }

  return result % m;
}

asserts(
  solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]),
  [true, false, false, true]
);

asserts(
  solution(
    ["apple", "banana", "cherry", "apple", "apple", "banana"],
    ["banana", "kiwi", "melon", "apple"]
  ),
  [true, false, false, true]
);
