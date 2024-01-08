const assert = require("assert");

/**
 * 이익의 조건으로는 처음 판매원으로부터 나온 10% 의 이익으로 전체 연결된 추천인들이 분배 되어야 한다.
 * 이익의 조건은 1이상일 경우 다음 추천인과 분배가 가능하다.
 * @param {*} enroll
 * @param {*} referral
 * @param {*} seller
 * @param {*} amount
 * @returns
 */

function solution(enroll, referral, seller, amount) {
  const adjacentList = new Map();
  enroll.forEach((seller, i) => {
    adjacentList.set(seller, { referral: referral[i], profit: 0 });
  });
  for (const idx in seller) {
    let initialAmount = amount[idx] * 100;
    let referral = adjacentList.get(seller[idx]);
    let profit = 0;
    while (initialAmount >= 1 && referral) {
      profit = Math.floor(initialAmount * 0.1); //10%
      referral.profit += initialAmount - profit;
      initialAmount = profit;
      referral = adjacentList.get(referral.referral);
    }
  }

  return enroll.map((seller) => adjacentList.get(seller).profit);
}

assert.deepEqual(
  solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
  ),
  [360, 958, 108, 0, 450, 18, 180, 1080]
);

assert.deepEqual(
  solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
  ),
  [0, 110, 378, 180, 270, 450, 0, 0]
);
