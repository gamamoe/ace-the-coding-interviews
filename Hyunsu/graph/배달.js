const assert = require("assert");
/**
 *
 * 접근 아이디어에 대한 구현에 모순이 있음을 알게됨
 * 아이디어 : 문제에서 요구하는건 K 이하로 배달이 가능한 마을의 개수 이니, 어떻게든 거쳐가더라도 K이하만 된다면 마을을 result에 포함시킨다.
 *
 * 어떻게든 거쳐가더라도 k이하만 되게 하는 방법에서 노드 5에 도착하는 경로는 여러개인데 a경로에서 먼저 5를 도착 했다고 하면,
 *
 *
 * @param {*} N
 * @param {*} road
 * @param {*} K
 * @returns
 */

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

/**
 * 통과 버전.
 * 노드의 방문 여부뿐만 아니라, 그 노드에 도달하는 데 드는 최소 비용도 함께 고려해야 함.
 * 구현 : visited 배열을 방문 여부 대신 해당 노드에 도달하는 최소 비용으로 사용
 * 새로운 경로가 발견될 때마다 이 최소 비용을 업데이트하는 방식
 *
 * Time Complexity : O(V^2 + E)
 * shift()대시 heap을 사용하여 O(lov V)로 최적화 가능
 * @param {} N
 * @param {*} road
 * @param {*} K
 * @returns
 */
function solution(N, road, K) {
  // adjacency list
  let adj_list = [];
  for (const [from, to, w] of road) {
    if (!adj_list[from]) adj_list[from] = [];
    adj_list[from].push([to, w]);
    if (!adj_list[to]) adj_list[to] = [];
    adj_list[to].push([from, w]);
  }
  let MAX_K = 500_001;
  let visited = Array.from({ length: N + 1 }, () => MAX_K);
  // bfs
  // queue
  let START = 1;
  let queue = [[START, 0]];

  // while
  while (queue.length) {
    let [v, w] = queue.shift();
    visited[v] = w;
    //인근 마을
    adj_list[v]?.forEach((info, i) => {
      // queue에 넣을 때 [마을, 현재 가중치 + 합산 가중치  ]
      const [adj_v, adj_w] = info;
      let future_w = w + adj_w;
      if (future_w <= K && future_w < visited[adj_v]) {
        queue.push([adj_v, future_w]);
      }
    });
  }

  return visited.filter((v) => v !== MAX_K).length;
}
