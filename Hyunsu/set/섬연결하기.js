const assert = require("assert");

/**
 * 잘못된 접근 방식
 * MST를 보고 난 후 접근의 문제점.
- 1. 정렬을 하지 않아 모든 노드의 find를 찾기 위해 거치는 가중치의 합을 구하는 부분에서 사이클핸들링이 어려웠음. - 이 부분은 가중치가 작은 순서대로 정렬로 접근.
- 2. 모든 엣지가 연결되어 있다는 점을 어느 시점에 알 수 있는지에 대한 의문을 해결하지 못했다. 이 부분은 양방향 인접리스트가 아닌 에지 리스트 형태로 유지해야 했었고 (사이클 핸들링이 쉬워짐), 모든 엣지가 연결되어 있다는 점은 트리와 그래프의 차이인 그래프 간선의 개수는 노드 개수보다 -1 개인점을 활용하여 해결.
 * @param {*} n
 * @param {*} costs
 * @returns
 */
function solution(n, costs) {
  var answer = 0;

  const disjoint = Array.from({ length: n }, (_, i) => i);
  const costArr = Array.from({ length: n }, () => 0);
  const adjacentArr = [];
  for (const c of costs) {
    const [island_a, island_b, cost] = c;

    if (!adjacentArr[island_a]) {
      adjacentArr[island_a] = [];
    }
    if (!adjacentArr[island_b]) {
      adjacentArr[island_b] = [];
    }

    adjacentArr[island_a].push([island_b, cost]);
    adjacentArr[island_b].push([island_a, cost]);
  }
  for (let i = 0; i < adjacentArr.length; i++) {
    const nodes = adjacentArr[i];
    const currentIsland = i;
    const islands = nodes.map((node) => node[0]);
    const costs = nodes.map((node) => node[1]);
    let min = Number.MAX_SAFE_INTEGER;
    let minIsland = Number.MAX_SAFE_INTEGER;
    for (const island of islands) {
      let cost =
        findAccCost(currentIsland, disjoint, costArr, 0) +
        findAccCost(island, disjoint, costArr, 0) +
        costs[islands.indexOf(island)];
      //싸이클 확인 필요  ❗️
      if (find(island, disjoint) === currentIsland) continue;
      if (cost < min) {
        min = cost;
        minIsland = island;
      }
    }
    //제일 작은 island가 disjoint의 root로 자기 자신이 있다면  continue
    if (find(minIsland, disjoint) === currentIsland) continue;
    union(minIsland, currentIsland, disjoint);
    costArr[currentIsland] =
      islands.indexOf(minIsland) === -1 ? 0 : costs[islands.indexOf(minIsland)];
  }
  return answer;
}
function findAccCost(target, disjoint, costArr, total) {
  if (disjoint[target] === target) return total;
  return (total = findAccCost(
    disjoint[target],
    disjoint,
    costArr,
    total + costArr[target]
  ));
}
function find(target, disjoint) {
  if (disjoint[target] === target) return target;
  return (disjoint[target] = find(disjoint[target], disjoint));
}
function union(current, root, disjoint) {
  disjoint[current] = root;
  return;
}

//✅ 크루스칼 알고리즘 반영
function solution1(n, costs) {
  var answer = 0;
  const disjoint = Array.from({ length: n }, (_, i) => i);
  let edgeNum = 0;
  //가중치 기준 내림차순 정렬 (pop()하기 위해 )
  costs.sort((a, b) => b[2] - a[2]);

  while (edgeNum < n - 1) {
    if (!costs.length) break;
    const [a, b, cost] = costs.pop();
    // 집합의 대표노드를 찾아 사이클인지 확인
    const rootA = find(a, disjoint);
    const rootB = find(b, disjoint);
    //사이클이 아니라면 union
    if (rootA !== rootB) {
      union(rootA, rootB, disjoint);
      edgeNum += 1;
      answer += cost;
    }
    // 사이클이라면 continue
  }
  return answer;
}

function find(target, disjoint) {
  if (disjoint[target] === target) return target;
  return (disjoint[target] = find(disjoint[target], disjoint));
}
function union(a, b, disjoint) {
  disjoint[a] = b;
  return;
}

assert.equal(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ]),
  4
);

assert.equal(
  solution(1, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ]),
  4
);
