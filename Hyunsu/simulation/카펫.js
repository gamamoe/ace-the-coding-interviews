/**
 * yellow의 가로, 세로를 만드는 모든 경우의 수에 대한 brown의 전체 길이를 구해 주어진 brown의 길이와 비교
 * TimeComplexity: O(yellow/2)
 * @param {*} brown
 * @param {*} yellow
 * @returns
 */
function solution(brown, yellow) {
  let yellow_w = 0;
  let brown_w = 0;
  let brown_h = 0;

  if (yellow === 1) {
    return [3, 3];
  }
  // yellow_h 를 1부터 yellow/2까지 반복
  for (let yellow_h = 1; yellow_h <= yellow / 2; yellow_h++) {
    //yellow의 가로 길이 구하기
    yellow_w = yellow / yellow_h;
    // yellow의 가로 길이가 세로 길이보다 작으면 continue
    if (yellow_h > yellow_w) continue;
    // brown의 가로, 세로 길이 구하기
    brown_w = yellow_w + 2;
    brown_h = yellow_h + 2;
    // brown의 가로, 세로 길이가 맞으면 break
    if (brown_w * 2 + brown_h * 2 - 4 === brown) break;

    yellow_w += 1;
  }
  return [brown_w, brown_h];
}
