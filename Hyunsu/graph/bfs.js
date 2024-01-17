const assert = require("assert");

/**
 * TimeComplexity
 * @param {*} graph
 * @param {*} start
 * @returns
 */
function solution(graph, start) {
  const adjList = {};
  graph.forEach(([from, to]) =>
    adjList[from] ? adjList[from].push(to) : (adjList[from] = [to])
  );
  const queue = [start];
  const result = [start]; //방문한 노드 담는 배열, bfs에서는 queue에 있는 노드는 이미 방문처리 완료.

  bfs(queue);
  return result;

  function bfs() {
    while (queue.length) {
      const nextList = adjList[queue.shift()];
      (nextList || []).forEach((next) => {
        if (result.includes(next)) return false; //이미 방문한 노드면 continue
        result.push(next); //방문처리
        queue.push(next); //방문처리
      });
    }
  }
}

assert.deepEqual(
  solution(
    [
      [1, 2],
      [1, 3],
      [2, 4],
      [2, 5],
      [3, 6],
      [3, 7],
      [4, 8],
      [5, 8],
      [6, 9],
      [7, 9],
    ],
    1
  ),
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
);

assert.deepEqual(
  solution(
    [
      [0, 1],
      [1, 2],
      [2, 3],
      [3, 4],
      [4, 5],
      [5, 0],
    ],
    1
  ),
  [1, 2, 3, 4, 5, 0]
);
