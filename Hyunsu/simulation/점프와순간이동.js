/**
 * 점프 할 때와 순간 이동 할 때의 모든 경우의 수에서 도착지점까지의 최소값을 구하는 방법으로 접근.
 * 문제는 숫자 N 이 10억이므로 DFS로는 시간초과..
 *
 *
 * @param {*} n
 * @returns
 */
function solution(n) {
  let minVals = [];
  dfs(1, 1);

  function dfs(curVal, curLocation) {
    if (curLocation === n) {
      minVals.push(curVal);
      return;
    }

    dfs(curVal + 1, curLocation + 1); //jump

    if (curLocation * 2 > n) {
      return;
    }
    dfs(curVal, curLocation * 2); //순간이동
  }
  return Math.min(...minVals);
}

solution(6);
