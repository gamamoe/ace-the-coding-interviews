/**
 * time complexity: O(n^2) 문제는 통과 .
 * n * 20 = 백만 * 20 = 2천만
 * @param {*} phone_book
 * @returns
 */
function solution(phone_book) {
  const set = new Set();
  // 길이가 짧은 순으로 정렬- 접두어가 될 수 있는 숫자를 set에서 찾기 위해
  phone_book.sort((a, b) => a.length - b.length);

  for (const phoneNum of phone_book) {
    if (set.has(phoneNum)) return false; //같은 번호 있으면 false

    let prefix = "";
    for (let i = 0; i < phoneNum.length; i++) {
      prefix += phoneNum[i];
      if (set.has(prefix)) return false;
    }
    set.add(phoneNum);
  }
  return true;
}

/**
 * 효율성 개선
 * some: 배열의 요소 중 하나라도 true이면 멈추고 true를 반환
 * 정렬 후, 다음 요소가 현재 요소로 시작하는 지 확인, 시작하면 true 반환 후 순회를 멈춘다.
 * 문제 요구 사항에서는 false로 반환해야 하므로 ! 연산자를 사용한다.
 * 마지막 요소까지 순회 했다는 것은, 이전 요소와 접두어 조건에 충족하지 않았다는 의미이므로, 더이상의 순회는 필요없음.
 * 따라서 마지막 요소를 순회했을 때는 false를 반환.
 *
 * TimeComplexity: O(nlogn)
 */
function solution1(phone_book) {
  return !phone_book.sort().some((t, i) => {
    if (i === phone_book.length - 1) return false; //마지막 인덱스는 false를 두어 무조건 true를 반환하지 않도록
    return phone_book[i + 1].startsWith(phone_book[i]);
  });
}

asserts.equal(solution(["119", "97674223", "1195524421"]), false);
asserts.equal(solution(["123", "456", "789"]), true);
asserts.equal(solution(["12", "123", "1235", "567", "88"]), false);
asserts.equal(solution(["12", "123", "1235", "567", "88"]), false);
asserts.equal(solution(["123", "456", "789"]), true);

asserts.equal(solution1(["119", "97674223", "1195524421"]), false);
asserts.equal(solution1(["123", "456", "789"]), true);
asserts.equal(solution1(["12", "123", "1235", "567", "88"]), false);
asserts.equal(solution1(["12", "123", "1235", "567", "88"]), false);
asserts.equal(solution1(["123", "456", "789"]), true);
