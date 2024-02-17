/**
 *  s를 업데이트 하여 1이 될 때까지 반복.
 *  반복 과정에는 0 을 "" 로 대체 한 문자열의 길이를 2진수로 변환하여 s에 대입한다.
 * TimeComplexity.. .? 잘 모르겠네요.
 * while문은 최악의 경우 O(n)이고, replaceAll은 O(n)
 * 최악의 경우 O(n^2)?
 * @param {*} s
 * @returns
 */

function solution(s) {
  let cnt = 0;
  let zeroCnt = 0;
  while (s !== "1") {
    zeroCnt += (s.match(/0/g) || []).length;
    s = s.replaceAll("0", "").length.toString(2);
    cnt += 1;
  }
  return [cnt, zeroCnt];
}
