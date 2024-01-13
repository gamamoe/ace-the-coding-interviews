const assert = require("assert");
const { PriorityQueue } = require("../utils/PriorityQueue");

function solution(graph, start) {
  //distance
  let distances = {};
  Object.keys(graph).forEach((v) => (distances[v] = Infinity));

  //paths
  const paths = { [start]: [start] };
  //heap
  const pq = new PriorityQueue();

  //출발 거리 초기화
  distances[start] = 0;
  // heap 처음 초기화
  pq.enqueue(0, start);

  while (pq.values.length > 0) {
    let { val: currentW, priority: currentV } = pq.dequeue();

    if (distances[currentV] < currentW) continue; //현재 distance가 더 작으면 continue
    //인접 리스트 순회
    (Object.keys(graph[currentV]) || []).forEach((nextV) => {
      let nextW = graph[currentV][nextV];

      // 다옴노드 가중치+현재 노드, 다음 노드 가중치 비교
      if (currentW + nextW < distances[nextV]) {
        //distance 테이블 갱신
        distances[nextV] = currentW + nextW;
        //paths  테이블 갱신
        paths[nextV] = [...paths?.[currentV], nextV];

        //pq 넣기
        pq.enqueue(currentW + nextW, nextV);
      }
    });
  }
  //키 기준 정렬
  const sortedPath = Object.keys(paths)
    .sort()
    .reduce((sortedObj, key) => {
      sortedObj[key] = paths[key];
      return sortedObj;
    }, {});

  return [distances, sortedPath];
}

assert.deepEqual(
  solution({ A: { B: 9, C: 3 }, B: { A: 5 }, C: { B: 1 } }, "A"),
  [
    { A: 0, B: 4, C: 3 },
    { A: ["A"], B: ["A", "C", "B"], C: ["A", "C"] },
  ]
);

assert.deepEqual(
  solution({ A: { B: 1 }, B: { C: 5 }, C: { D: 1 }, D: {} }, "A"),
  [
    { A: 0, B: 1, C: 6, D: 7 },
    { A: ["A"], B: ["A", "B"], C: ["A", "B", "C"], D: ["A", "B", "C", "D"] },
  ]
);
