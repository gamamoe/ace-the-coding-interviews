/*
* 부분 배낭 문제
* 주어진 무게 제한을 초과하지 않으면서 가치가 최대가 되도록 물건을 넣는 문제
* 각 물건은 무게와 가치로 표현된다.
* 물건은 쪼갤 수 있으므로 물건의 일부분이 담길 수 있다.

*/
function fractional_knapsack(items, limit) {
  let total_v = 0;
  // 무게당 가치 계산
  items.forEach((item) => item.push(item[1] / item[0]));
  // 무게당 가치로 내림차순 정렬
  items.sort((a, b) => b[2] - a[2]);
  for (const [w, v, _v] of items) {
    if (w <= limit) {
      total_v += v;
      limit -= w;
    } else {
      total_v += _v * limit;
      break;
    }
  }
  return Math.round(total_v * 100) / 100;
}

console.log(
  fractional_knapsack(
    [
      [10, 19],
      [7, 10],
      [6, 10],
    ],
    15,
  ),
); //27.33
console.log(
  fractional_knapsack(
    [
      [10, 60],
      [20, 100],
      [30, 120],
    ],
    50,
  ),
); //240
