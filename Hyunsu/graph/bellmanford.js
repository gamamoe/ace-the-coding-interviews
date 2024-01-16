const assert = require("assert");

function solution(graph, source) {
  // 길이 리스트
  let distances = Array.from({ length: graph.length }, () => Infinity);
  // edge 길이
  let edgeLen = graph.length - 1;
  // 경로 순서 리스트
  let sources = Array.from({ length: graph.length }, () => "None");
  // 출발 노드 길이 0으로 초기화
  distances[0] = 0;
  // edge길이 만큼 순회
  for (let i = 0; i < edgeLen; i++) {
    for (let j = 0; j < graph.length; j++) {
      for (const [next, w] of graph[j]) {
        //infinity가 아니고 현재노드 길이+가중치 < 다음 노드 길이 이면  다음 노드 길이 = 현재 노드 길이 + 가중치  갱신

        if (distances[j] !== Infinity && distances[j] + w < distances[next]) {
          distances[next] = distances[j] + w; // 최단 거리 갱신 j->next
          sources[next] = j; // 방문 경로 저장
        }
      }
    }
  }

  // 사이클인지 확인
  // let isCycle = false;
  // edge 길이 만큼 순회
  for (let j = 0; j < graph.length; j++) {
    for (const [next, w] of graph[j]) {
      //infinity가 아니고 현재노드 길이+가중치 < 다음 노드 길이 이면  다음 노드 길이 = 현재 노드 길이 + 가중치  갱신
      if (distances[j] !== Infinity && distances[j] + w < distances[next]) {
        return [-1];
      }
    }
  }

  return [distances, sources];
}

assert.deepEqual(
  solution(
    [
      [
        [1, 4],
        [2, 3],
        [4, -6],
      ],
      [[3, 5]],
      [[1, 2]],
      [
        [0, 7],
        [2, 4],
      ],
      [[2, 2]],
    ],
    0
  ),
  [
    [0, -2, -4, 3, -6],
    ["None", 2, 4, 1, 0],
  ]
);

assert.equal(
  solution([
    [
      [1, 5],
      [2, -1],
    ],
    [[2, 2]],
    [[3, -2]],
    [
      [0, 2],
      [1, 6],
    ],
  ]),
  -1
);
