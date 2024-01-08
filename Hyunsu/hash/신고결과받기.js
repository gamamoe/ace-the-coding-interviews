const asserts = require("assert");

/** 처리 결과 메일을 받은 횟수
 *
 * @param {*} id_list
 * @param {*} report
 * @param {*} k
 * @returns
 */
function solution(id_list, report, k) {
  let reportCount = {}; // 신고 당한 횟수 table
  var answer = [];
  let dashBoard = {}; // {이용자 id: 신고한id[]}

  for (const id of id_list) {
    dashBoard[id] = [];
  }
  //report를 순회하면서, 신고당한 횟수 count , dashBaord에 이용자id와 신고한 id업데이트
  report.forEach((singleReport) => {
    const [from, to] = singleReport.split(" ");
    if (dashBoard[from].indexOf(to) > -1) return false; // 이용자 id과 신고한id가 중복일 경우 처리
    reportCount[to] = (reportCount[to] || 0) + 1;
    dashBoard[from].push(to);
  });

  Object.keys(dashBoard).map((id) => {
    //id순회
    let cnt = 0;
    dashBoard[id].forEach((id) => {
      reportCount[id] >= k ? (cnt += 1) : cnt;
    });
    answer.push(cnt);
  });

  return answer;
}

asserts.deepEqual(
  solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2
  ),
  [2, 1, 1, 0]
);
