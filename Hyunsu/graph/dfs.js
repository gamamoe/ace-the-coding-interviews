const assert = require("assert");
/**
 * [출발, 도착]
 * 노드의 최대 개수 <=100
 * ASCII를 이용하여 방문 여부 처리 방식
 * TimeComplexity: O(V+E)
 */

function solution(graph, start) {
  //인접 리스트로 변환
  const adjList = {};
  graph.forEach(([from, to]) =>
    adjList[from] ? adjList[from].push(to) : (adjList[from] = [to])
  );
  const result = ["A"];
  const visited = ["A"];

  //graph[start] 를 시작으로  dfs탐색
  return dfs(start, visited, result);

  function dfs(v, visited, result = []) {
    (adjList[v] || []).forEach((w) => {
      let index = charCode(w);
      if (!visited[index]) {
        //방문처리
        visited[index] = w;
        result.push(w);
        //방문 하지 않은경우
        result = dfs(w, visited, result);
      }
    });
    return result;
  }
}

function charCode(char) {
  return char.charCodeAt() - 65;
}

/**
 * 책의 set자료구조를 이용한 방문 처리 방식
 * TimeComplexity: O(V+E)
 * @param {*} graph
 * @param {*} start
 * @returns
 */
function solution2(graph, start) {
  const result = [];
  const adjList = {};
  //인접리스트 초기화
  graph.forEach(([from, to]) =>
    adjList[from] ? adjList[from].push(to) : (adjList[from] = [to])
  );

  dfs(start, new Set()); //set 자료구조를 이용하여 중복 방문처리
  return result;

  function dfs(v, visited = []) {
    if (!v) return null;
    //방문 처리
    visited.add(v);
    result.push(v);
    //인접 노드 탐색
    (adjList[v] || []).forEach((w) =>
      !visited.has(w) ? dfs(w, visited) : null
    );
  }
}

/**
 * Stack을 이용한 dfs
 * O(E) + O(V)
 */

function dfs(graph, start) {
  const adjList = {};
  graph.forEach(([from, to]) =>
    adjList[from] ? adjList[from].push(to) : (adjList[from] = [to])
  );

  const result = [];
  const stack = [start];
  while (stack.length) {
    const top = stack.pop();
    result.push(top);
    if (visited[top]) continue;
    visited[top] = 1; //방문처리
    //인접 노드 탐색
    stack.push(...(adjList[top] || [])); // 방문할 노드를 스택에 모두 넣는다.
  }
}

assert.deepEqual(
  dfs(
    [
      ["A", "B"],
      ["B", "C"],
      ["C", "D"],
      ["D", "E"],
    ],
    "A"
  ),
  ["A", "B", "C", "D", "E"]
);

assert.deepEqual(
  dfs(
    [
      ["A", "B"],
      ["A", "C"],
      ["B", "D"],
      ["B", "E"],
      ["C", "F"],
      ["E", "F"],
    ],
    "A"
  ),
  ["A", "B", "D", "E", "F", "C"]
);

assert.deepEqual(
  solution2(
    [
      ["A", "B"],
      ["B", "C"],
      ["C", "D"],
      ["D", "E"],
    ],
    "A"
  ),
  ["A", "B", "C", "D", "E"]
);

assert.deepEqual(
  solution2(
    [
      ["A", "B"],
      ["A", "C"],
      ["B", "D"],
      ["B", "E"],
      ["C", "F"],
      ["E", "F"],
    ],
    "A"
  ),
  ["A", "B", "D", "E", "F", "C"]
);

assert.deepEqual(
  solution(
    [
      ["A", "B"],
      ["B", "C"],
      ["C", "D"],
      ["D", "E"],
    ],
    "A"
  ),
  ["A", "B", "C", "D", "E"]
);

assert.deepEqual(
  solution(
    [
      ["A", "B"],
      ["A", "C"],
      ["B", "D"],
      ["B", "E"],
      ["C", "F"],
      ["E", "F"],
    ],
    "A"
  ),
  ["A", "B", "D", "E", "F", "C"]
);
