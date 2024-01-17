/**
 * 시간복잡도 : O(n)
 * visited 를 통해 각 노드마다 한번만 방문
 */
const assert = require("assert");

function solution(n, computers) {
  const visited = Array.from({ length: n }, () => 0);
  let cnt = 0;
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      //방문하지 않은 노드만 dfs 탐색
      dfs(i);
      cnt += 1;
    }
  }
  return cnt;
  function dfs(v) {
    visited[v] = 1;
    //인접 노드 탐색, 연결된 노드 &&  방문하지 않은 노드 dfs 탐색, 아닐경우 false를 통해 다음 노드 처리
    (computers[v] || []).forEach((value, idx) =>
      !!value && !visited[idx] ? dfs(idx) : false
    );
  }
}

assert.equal(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ]),
  2
);

assert.equal(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ]),
  1
);
