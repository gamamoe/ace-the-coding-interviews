const assert = require("assert");

function solution(N, stages) {
  const count = Array(N + 1).fill(0);

  for (let stage of stages) {
    if (stage === N + 1) continue; // 모든스테이지 도달한 유저 제외
    count[stage] += 1;
  }
  let failureRates = [];
  let failure;
  let completedPlayersNum = stages.length;
  for (let i = 1; i < count.length; i++) {
    failure =
      completedPlayersNum == 0 ? 0 : (failure = count[i] / completedPlayersNum);
    failureRates.push([i, failure]);
    completedPlayersNum -= count[i];
  }

  return failureRates.sort((a, b) => b[1] - a[1]).map((v) => v[0]);
}

assert.deepEqual(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5]);
