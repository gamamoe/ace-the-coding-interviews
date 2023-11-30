const assert = require("assert");

/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 * time complexity: O(n)
 * space complexity: O(n)
 */
var duplicateZeros = function (arr) {
  let duplicateZeroArray = [];
  for (let i = 0; i < arr.length; i++) {
    let value = arr[i];
    duplicateZeroArray.push(value);

    if (value === 0) {
      duplicateZeroArray.push(0);
    }
  }

  for (let i = 0; i < arr.length; i++) {
    arr[i] = duplicateZeroArray[i];
  }
};

/**
 * optimize space complexity to O(1)
 * in-place
 * hint를 다 봐도 못풀었음.
 * solution의 접근법 본 후 구현 시도
 * 구현이 어려웠던 이유: 0을 포함 한다고 가정했을 때, array에서 사용되는 가장 마지막 인덱스의 값이 0 이라면,
 * fixed array length를 맞추기 위해 0을 복사할지, 안할지를 결정해야 하는 엣지케이스 생각못함.
 * memory 성능: 평균 44ms으로 space complexity O(n) 과 비슷한 성능
 * @param {*} arr
 */
var duplicateZeros1 = function (arr) {
  let lengthWithZero = 0;
  let lastIndex = 0;

  // 0을 포함했을 때 fixed array의 마지막 인덱스에 올 수 있는 인덱스 찾기
  for (const index in arr) {
    if (arr[index] === 0) {
      lengthWithZero += 2;
    } else {
      lengthWithZero += 1;
    }
    if (lengthWithZero >= arr.length) {
      lastIndex = index;
      break;
    }
  }

  let shouldDuplicateZeroAtLastIndex =
    lengthWithZero === arr.length && arr[lastIndex] === 0; //edge case: 마지막 인덱스가 0인 경우, 0을 복사할지 복사하지 않을지
  let currentIndex = lastIndex;
  let zeroFlag = false;

  for (let i = arr.length - 1; i >= 0; i--) {
    if (zeroFlag) {
      arr[i] = 0;
      zeroFlag = false;
      continue;
    }

    arr[i] = arr[currentIndex];
    // 이미 0이 들어간 상태에서 마지막 인덱스가 0 이라면, zeroFlag를 무시해야 한다.
    if (shouldDuplicateZeroAtLastIndex && currentIndex === lastIndex) {
      zeroFlag = true;
    }
    if (arr[currentIndex] === 0 && currentIndex !== lastIndex) {
      zeroFlag = true;
    }
    currentIndex -= 1;
  }
  return arr;
};

assert.deepEqual(
  duplicateZeros1([1, 0, 2, 3, 0, 4, 5, 0]),
  [1, 0, 0, 2, 3, 0, 0, 4]
);
assert.deepEqual(
  duplicateZeros1([0, 4, 1, 0, 0, 8, 0, 0, 3]),
  [0, 0, 4, 1, 0, 0, 0, 0, 8]
);
assert.deepEqual(
  duplicateZeros1([8, 4, 5, 0, 0, 0, 0, 7]),
  [8, 4, 5, 0, 0, 0, 0, 0]
);

assert.deepEqual(
  duplicateZeros1([1, 5, 2, 0, 6, 8, 0, 6, 0]),
  [1, 5, 2, 0, 0, 6, 8, 0, 0]
);
