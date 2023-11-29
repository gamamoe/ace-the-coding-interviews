const assert = require("assert");

function solution(arr1, arr2) {
  // arr1의 row, arr2의 col 길이로 answer 배열 만들기
  let answer = Array.from({ length: arr1.length }, () =>
    Array(arr2[0].length).fill(0)
  );
  // arr1의 row, arr2의 col 길이만큼 반복문 돌리기
  for (let row = 0; row < arr1.length; row++) {
    for (let col = 0; col < arr2[0].length; col++) {
      let rowArr = arr1[row];
      let colArr = getCols(arr2, col); //col 이 일치하는 arr2의 열을 가져옴.
      answer[row][col] = calculate(rowArr, colArr);
    }
  }
  return answer;
}

function calculate(row, col) {
  let sum = 0;
  for (let i = 0; i < row.length; i++) {
    sum += row[i] * col[i];
  }
  return sum;
}

function getCols(arr, col) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (j === col) {
        result.push(arr[i][j]);
      }
    }
  }
  return result;
}

//test
assert.deepEqual(
  solution(
    [
      [1, 4],
      [3, 2],
      [4, 1],
    ],
    [
      [3, 3],
      [3, 3],
    ]
  ),
  [
    [15, 15],
    [15, 15],
    [15, 15],
  ]
);

assert.equal(
  getCols(
    [
      [1, 2, 3],
      [4, 5, 6],
    ],
    1
  ),
  [2, 5]
);

assert.equal(calculate([1, 2, 3], [2, 3, 4]), 20);
