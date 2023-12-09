/**
 * js의 shift()메서드 O(n)를 이용.
 * 모수가 작아서 그런지 테스트에는 통과.
 * @param {*} cards1
 * @param {*} cards2
 * @param {*} goal
 * @returns
 */
function solution(cards1, cards2, goal) {
  for (const word of goal) {
    const hasWordCard1 = hasWord(word, cards1);
    const hasWordCard2 = hasWord(word, cards2);

    if (!hasWordCard1 && !hasWordCard2) return "No";

    if (hasWordCard1) {
      shift(cards1);
      continue;
    }
    if (hasWordCard2) {
      shift(cards2);
      continue;
    }
  }
  return "Yes";
}

function hasWord(word, arr) {
  return arr[0] === word;
}

function shift(arr) {
  return arr.shift();
}

/**
 * dequeue를 이용한 문제 풀이
 *
 */
