const assert = require("assert");
const Queue = require("../lib/queue");

/**
 * timeComplexity: O(n*k)
 * @param {*} n 인원 수
 * @param {*} k 번째 사람 - 소거되어야 하는 사람
 * @returns
 */
function solution(n, k) {
  const queue = new Queue();
  //O(n)
  for (let i = 1; i <= n; i++) {
    queue.enqueue(i);
  }

  //O(n)
  while (queue.length() > 1) {
    let count = k;
    //O(k)
    while (count > 0) {
      count -= 1;
      if (count === 0) {
        queue.dequeue();
      } else {
        queue.enqueue(queue.dequeue());
      }
    }
  }

  return queue.dequeue();
}

assert(solution(5, 2), 3);
