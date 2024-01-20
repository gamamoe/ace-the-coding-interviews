const assert = require("assert");
/**
 *
 * @param {*} n
 * @param {*} wires
 * @returns
 */
function solution(n, wires) {
  let adj_list = Array.from({ length: n + 1 }, () => []);
  wires.forEach(([from, to]) => {
    adj_list[from].push(to);
    adj_list[to].push(from);
  });

  let mins = [];
  // wires를 순회하면서 간선 빼기
  wires.forEach((wire) => {
    let visited = new Set();
    let deep_copy_adj = adj_list.map((row) => row.slice());
    const [a, b] = wire;
    deep_copy_adj[a].splice(deep_copy_adj[a].indexOf(b), 1);
    deep_copy_adj[b].splice(deep_copy_adj[b].indexOf(a), 1);
    let subtraction = 0;
    //연결되어진 노드 개수 구하기
    for (let i = 1; i <= n; i++) {
      if (visited.has(i)) continue; // 방문한 노드면 continue
      let result1 = dfs(i, 0, deep_copy_adj, visited); // 연결 노드 개수
      subtraction = result1 - subtraction; //첫 집합은 subtraction으로 할당, 두번 째 집합은 빼기
    }
    mins.push(Math.abs(subtraction));
  });
  return Math.min(...mins);

  function dfs(i, level, adj_list, visited) {
    visited.add(i);
    level += 1;

    adj_list[i].forEach((v) => {
      if (visited.has(v)) return false;
      level = dfs(v, level, adj_list, visited);
    });
    return level;
  }
}

assert.equal(
  solution([
    [],
    [3],
    [2],
    [1, 2, 4],
    [3, 5, 6, 7],
    [4],
    [4],
    [4, 8, 9],
    [7],
    [7],
  ]),
  3
);
assert.equal(
  solution([
    [1, 2],
    [2, 3],
    [3, 4],
  ]),
  0
);
assert.equal(
  solution([
    [1, 2],
    [2, 7],
    [3, 7],
    [3, 4],
    [4, 5],
    [6, 7],
  ]),
  1
);
