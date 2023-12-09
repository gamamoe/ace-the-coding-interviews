const assert = require("assert");
/**
 * 정확성: 29/30, 효율성 5/10
 * index 접근 방식 하지만 불필요한 연산 (삭제된 행을 찾는데, row를 순회하면서 찾는다.)이 많음
 * @param {*} n
 * @param {*} k
 * @param {*} cmd
 * @returns
 */
function solution(n, k, cmd) {
  var answer = "";
  let current = k;
  let row = Array.from({ length: n }, (v, i) => i);
  let deletedStack = [];
  for (const index in cmd) {
    const [direction, num = 0] = cmd[index].split(" ");
    if (direction === "D") {
      let temp = 0;
      let count = Number(num);
      while (count > 0 && current < row.length) {
        current = current += 1;
        if (row[current]) {
          count--;
        }
      }
      continue;
    }
    if (direction === "U") {
      let count = Number(num);

      while (count > 0 && current >= 0) {
        current = current - 1;
        if (row[current]) {
          count -= 1;
        }
      }
      continue;
    }
    if (direction === "C") {
      deletedStack.push([current, row[current]]);

      delete row[current];

      //find next current
      let tempCurrent = current;
      let isFound = false;
      while (tempCurrent < row.length) {
        if (row[tempCurrent]) {
          isFound = true;
          break;
        }
        tempCurrent += 1;
      }
      if (isFound) {
        current = tempCurrent;
      } else {
        let temp = current;
        //반대로 작아져야 함.
        while (temp >= 0) {
          if (row[temp]) {
            current = temp;
            break;
          }
          temp--;
        }
      }
      continue;
    }
    if (direction === "Z") {
      //current는 변경 x
      //restore
      const currentValue = row[current];
      if (!deletedStack.length) continue;
      const [index, value] = deletedStack.pop();
      row[index] = value;
      continue;
    }
  }
  // compare
  for (const num of row) {
    if (num === undefined) {
      answer += "X";
    } else {
      answer += "O";
    }
  }
  return answer;
}
//delete를 사용하고 undefined 면 넘어가서 value가 나올 때까지 찾기,
/**
 *
 * Optimized solution
 * 삭제된 행에 대하여 LinkedList 개념을 활용하여 다음 row를 바로 지정 .불필요한 연산을 줄임.
 * 책 풀이 참고
 * @param {*} n
 * @param {*} k
 * @param {*} cmd
 * @returns
 */
function solution1(n, k, cmd) {
  var answer = Array(n).fill("O");
  let current = k + 1;
  let deletedStack = [];
  let up = Array.from({ length: n + 2 }, (v, i) => i - 1);
  let down = Array.from({ length: n + 1 }, (v, i) => i + 1);

  for (const index in cmd) {
    const [direction, num = 0] = cmd[index].split(" ");

    if (direction === "C") {
      deletedStack.push(current);
      up[down[current]] = up[current];
      down[up[current]] = down[current];
      current = n < down[current] ? up[current] : down[current];
      continue;
    }
    if (direction === "Z") {
      const deletedRow = deletedStack.pop();
      down[up[deletedRow]] = deletedRow;
      up[down[deletedRow]] = deletedRow;
      continue;
    }

    if (direction === "U") {
      for (let i = 0; i < Number(num); i++) {
        current = up[current];
      }
      continue;
    }
    if (direction === "D") {
      for (let i = 0; i < Number(num); i++) {
        current = down[current];
      }
      continue;
    }
  }
  //삭제된 행은 deletedStack에서 찾는다.

  while (deletedStack.length) {
    const row = deletedStack.pop();
    answer[row - 1] = "X";
  }
  return answer.join("");
}

// solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]);
assert.equal(
  solution1(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]),
  "OOOOXOOO"
);
assert.equal(
  solution1(8, 2, [
    "D 2",
    "C",
    "U 3",
    "C",
    "D 4",
    "C",
    "U 2",
    "Z",
    "Z",
    "U 1",
    "C",
  ]),
  "OOXOXOOO"
);
