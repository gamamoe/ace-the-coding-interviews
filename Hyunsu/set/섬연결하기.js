const assert = require("assert");

/**
 * 잘못된 접근 방식
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
