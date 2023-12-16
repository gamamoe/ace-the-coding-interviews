const assert = require("assert");
const { setEngine } = require("crypto");

/**
 * 예제 케이스만 맞고, 실패
 * 1.각 손님에 대한 주문에서, 단품메뉴 조합 구하기
 *   - 1번손님 : 2개조합, 3개조합, 4개조합
 *   - 2번손님 : 2개조합, 3개조합, 4개조합
 *   조합을 담는 해시테이블 만들기
 *   원소에 저장되는 문자열 오름차순 정렬 유의 -  "AB" 조합만들때 오름차순
 *   menuCombFreq = {  2: { "AB": 2, "BC": 3},
 *                     3: {"ABC":2}
 *     }
 *
 * 2. 2개 조합 , 3개 조합, 4개조합에서 가장 많이 시킨 메뉴 뽑아 오기 ( 개수가 같다면 여러개 가져오기) - 배열에 저장
 * 3. 배열을 다시 오름차순으로 정렬
 *
 *
 *
 * @param {*} orders
 * @param {*} course
 */
function solution(orders, course) {
  const menuCombFreq = {};
  for (let order of orders) {
    for (let numOfCourse of course) {
      order = order.split("").sort().join("");
      const menuCombs = getMenuComb(order, numOfCourse);
      //  각 조합개수에 대한 hashTable 초기화, 2: { "AB": 2, "BC": 3}
      for (menu of menuCombs) {
        if (!menuCombFreq[numOfCourse]) menuCombFreq[numOfCourse] = new Map();

        let courseMapper = menuCombFreq[numOfCourse];
        // 같은 메뉴 조합이 있으면+1, 아니면 1
        courseMapper.set(menu, (courseMapper.get(menu) || 0) + 1);
      }
    }
  }

  let topMenus = [];
  // menu조합이 다 끝난후, 각 음식조합개수 마다, 가장 많이 시킨 음식 정렬
  // 각 코스마다 최대 오더 수 가져오기
  Object.keys(menuCombFreq).forEach((numOfCourse) => {
    const courseMapper = menuCombFreq[numOfCourse];
    // 코스에 대한 최대 오더수
    let maxOrder = Math.max(...courseMapper.values());
    if (maxOrder < 2) return false; //최소 2명 이상의 손님에게 받은 메뉴 조건
    // 최대 오더수와 동일하면 top Menu에 넣기
    courseMapper.forEach((freq, menu) => {
      if (freq !== maxOrder) return false;
      topMenus.push(menu);
    });
  });
  return topMenus.sort();
}

function getMenuComb(orders, numCourse) {
  // numCourse C orders (Comb)
  let visited = Array(orders.length).fill(false);
  let combs = [];
  let selected = [];
  dfs(orders, numCourse, 0, selected, visited);

  function dfs(str, level, start, selected, visited) {
    if (level === 0) {
      const MenuInChar = selected.join("");
      combs.push(MenuInChar);
      return;
    }

    for (let i = start; i < str.length; i++) {
      if (visited[i]) continue;
      visited[i] = true;
      selected.push(str[i]);
      dfs(str, level - 1, i + 1, selected, visited);
      visited[i] = false;
      selected.pop();
    }
  }

  return combs;
}

/**
 *  책 접근 법 풀이+ 다른 사람 풀이
 *  코스 조합 수에 대한 손님 수로 iterate하는게 더 수월한느낌..?
 *  책접근
 *  2개 : 1번손님 2개 조합, 2번 손님 2개조합, 3번손님 2개조합
 *  3개 : 1번손님 3개조합 , 2번손님 3개조합..
 *
 * => {2개 : { "AB" :}}
 *
 * 다른 사람 풀이 : 출현 횟수의 max를 dfs내에서 미리 했음.
 *
 * 효율성은 비슷 (첫번째 솔루션(0.6 - 6ms, 33-37), 두번째 솔루션 (0.5-10ms, )
 *
 * @param {*} orders
 * @param {*} course
 */
function solution1(orders, course) {
  let visited = Array(orders.length).fill(false);
  let selected = [];
  let menuFreqMapper = {};
  let finalMenuFreqMapper = {};
  let maxFreq = Array(10 + 1).fill(0);

  for (let c of course) {
    for (let o of orders) {
      o = o.split("").sort().join("");
      dfs(o, c, 0);
      // 구성이 몇 번 주문되었는지
      finalMenuFreqMapper;
    }
  }
  let answer = Object.keys(finalMenuFreqMapper).filter(
    (menu) => maxFreq[menu.length] === finalMenuFreqMapper[menu]
  );
  return answer.sort();

  function dfs(str, level, start) {
    if (level === 0) {
      const menu = selected.join("");
      menuFreqMapper[menu] = (menuFreqMapper[menu] || 0) + 1;
      // 같은 메뉴 출현 횟수 max값 갱신 최적화
      if (menuFreqMapper[menu] >= 2) {
        maxFreq[selected.length] = Math.max(
          maxFreq[selected.length],
          menuFreqMapper[menu]
        );
        finalMenuFreqMapper[menu] = menuFreqMapper[menu];
      }

      return;
    }

    for (let i = start; i < str.length; i++) {
      if (visited[i]) continue;
      visited[i] = true;
      selected.push(str[i]);
      dfs(str, level - 1, i + 1);
      visited[i] = false;
      selected.pop();
    }
  }
}

assert.deepStrictEqual(
  solution1(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]),
  ["AC", "ACDE", "BCFG", "CDE"]
);

// assert.deepEqual(getMenuComb("CDE", 2), ["CD", "CE", "DE"]);
// assert.deepEqual(getMenuComb("DCE", 2));
