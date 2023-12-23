/**
 * availableNodes 를 이용하여 현재 노드에서 갈 수 있는 노드를 저장
 *
 * @param {*} info
 * @param {*} edges
 * @returns
 */
function solution(info, edges) {
  let queue = [];
  let adjacentList = {};
  for (const [from, to] of edges) {
    adjacentList[from] = adjacentList[from] || [];
    adjacentList[from].push(to);
  }

  let max = 0;
  queue = [{ node: 0, curShip: 1, curWolf: 0, availableNodes: [] }];

  while (queue.length) {
    let { node, curShip, curWolf, availableNodes } = queue.shift();
    max = Math.max(max, curShip);
    let nextNodes = adjacentList[node];
    if (nextNodes) availableNodes = [...availableNodes, ...nextNodes];

    for (const nextNode of availableNodes) {
      if (info[nextNode]) {
        if (curShip !== curWolf + 1) {
          let n = [...availableNodes];
          let removeItem = n.indexOf(nextNode);
          n.splice(removeItem, 1);
          queue.push({
            node: nextNode,
            curShip,
            curWolf: curWolf + 1,
            availableNodes: n,
          });
        }
      } else {
        let n = [...availableNodes];
        let removeItem = n.indexOf(nextNode);
        n.splice(removeItem, 1);
        queue.push({
          node: nextNode,
          curShip: curShip + 1,
          curWolf,
          availableNodes: n,
        });
      }
    }
  }

  return max;
}

solution(
  [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
  [
    [0, 1],
    [1, 2],
    [1, 4],
    [0, 8],
    [8, 7],
    [9, 10],
    [9, 11],
    [4, 3],
    [6, 5],
    [4, 6],
    [8, 9],
  ]
);
