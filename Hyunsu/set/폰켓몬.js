/**
 * 주어진 배열에서 포켓몬 종류 개수를 세어 n/2 보다 작으면 포켓몬 종류 개수를 , 크다면 최대 포켓몬 종류를 선택하는 n/2를 리턴.
 * 길이가 10,000 이하이니 O(n)가능
 * 해시테이블을 사용하여 포켓몬 종류 세기
 * @param {*} nums
 * @returns
 */
function solution(nums) {
  const hashTable = {};

  for (const num of nums) {
    hashTable[num] = (hashTable[num] || 0) + 1;
  }

  const pocketmonSpeicesNum = Object.keys(hashTable).length;
  return pocketmonSpeicesNum > nums.length / 2
    ? nums.length / 2
    : pocketmonSpeicesNum;
}
