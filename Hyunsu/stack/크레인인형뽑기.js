const assert = require("assert");
/**
 * 1차 풀이
 * @param {*} board
 * @param {*} moves
 * @returns
 */

function solution(board, moves) {
  let answer = 0;
  let basket = [];
  for (const move of moves) {
    let col = move - 1;

    //row 찾기
    let row = 0;
    let toy = 0;
    while (row < board.length) {
      if (board[row][col] > 0) {
        toy = board[row][col];
        board[row][col] = 0; //mutate to 0
        break;
      }
      row += 1;
    }
    if (!toy) continue;

    // stack 에 넣기
    if (basket.length > 0 && basket[basket.length - 1] === toy) {
      basket.pop();
      answer += 2;
      continue;
    }
    basket.push(toy);
  }
  return answer;
}

/**
 *  2차 리팩토링
 * 함수 나누기.
 */

function solution1(board, moves) {
  let answer = 0;
  let basket = [];
  for (const move of moves) {
    const col = move - 1;
    const row = moveCraneToFindRow(col, board);
    const toy = pickToy(row, col, board);
    if (!toy) continue;

    mutateBoard(row, col, board);
    const { score } = putToyInBasket(
      hasSameToyInBasket(basket, toy),
      () => basket.pop(),
      () => basket.push(toy)
    );

    answer += score;
  }
  return answer;
}

function mutateBoard(row, col, board) {
  board[row][col] = 0;
}
function moveCraneToFindRow(col, board) {
  let row = 0;
  while (row < board.length) {
    if (board[row][col] > 0) {
      return row;
    }
    row += 1;
  }
  return 0;
}
function pickToy(row, col, board) {
  if (row >= board.length || row < 0 || col >= board[0].length || col < 0)
    return 0;
  return board[row][col];
}

function hasSameToyInBasket(basket, toy) {
  return basket.length > 0 && basket[basket.length - 1] === toy;
}
// 찾은 장난감을 basket안에 넣는데, 만약 bakset에 장난감이 있고, basket의 마지막 장난감과 같다면, basket에서 장난감을 빼고, answer에 2를 더한다.
function putToyInBasket(condition, truFn, falseFn) {
  if (condition) {
    truFn();
    return { score: 2 };
  }
  falseFn();
  return { score: 0 };
}

assert.equal(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  ),
  4
);

assert.equal(
  moveCraneToFindRow(0, [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ]),
  3
);

assert.equal(
  pickToy(6, 0, [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ]),
  0
);
