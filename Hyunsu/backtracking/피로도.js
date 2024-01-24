const assert = require("assert");

function solution(k, dungeons) {
  let visited = new Set();

  return dfs(0, k, 0, visited, 0);

  function dfs(level, cur, cnt, visited, max) {
    for (let i = 0; i < dungeons.length; i++) {
      const [required, consumed] = dungeons[i];
      if (visited.has(i)) continue;
      // 현재피로도와 최소 필요 피로도 비교
      if (cur < required) continue;

      visited.add(i);
      cnt += 1;
      max = Math.max(max, visited.size);
      max = dfs(level + 1, cur - consumed, cnt, visited, max);
      visited.delete(i);
    }
    return max;
  }
}

assert.equal(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ]),
  3
);
