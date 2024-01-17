const assert = require("assert");

function solution(N, road, K) {
  // adjacency list
  let adj_list = [];
  for (const [from, to, w] of road) {
    if (!adj_list[from]) adj_list[from] = [];
    adj_list[from].push([to, w]);
    if (!adj_list[to]) adj_list[to] = [];
    adj_list[to].push([from, w]);
  }
  console.log("adj_list", adj_list);
  let visited = Array.from({ length: N + 1 }, () => 0);
  // bfs
  // queue
  let START = 1;
  let queue = [[START, 0]];
  let pathSet = new Set();
  pathSet.add(START);

  // while
  while (queue.length) {
    let [v, w] = queue.shift();
    visited[v] = 1;
    //인근 마을
    adj_list[v]?.forEach((info, i) => {
      // queue에 넣을 때 [마을, 현재 가중치 + 합산 가중치  ]
      const [adj_v, adj_w] = info;
      let future_w = w + adj_w; //bfs경로를 통한 누적 가중치 + 노드가 가진 가중치
      //방문 안한 경우
      if (visited[adj_v]) return false;
      // 가중치 조건 적용 <=K
      if (future_w > K) return false;
      queue.push([adj_v, future_w]);
      pathSet.add(adj_v);
    });
  }
  return pathSet.size;
}

assert.equal(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  ),
  4
);
assert.equal(
  solution(
    6,
    [
      [1, 2, 1],
      [1, 3, 2],
      [2, 3, 2],
      [3, 4, 3],
      [3, 5, 2],
      [3, 5, 3],
      [5, 6, 1],
    ],
    4
  ),
  4
);

assert.equal(solution(2, [[1, 2, 4]], 3), 1);

assert.equal(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    5
  ),
  5
);

assert.equal(
  solution(
    6,
    [
      [1, 2, 1],
      [1, 3, 2],
      [2, 3, 2],
      [3, 4, 3],
      [3, 5, 2],
      [3, 5, 3],
      [5, 6, 1],
    ],
    6
  ),
  6
);
