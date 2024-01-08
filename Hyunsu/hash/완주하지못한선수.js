const asserts = require("fs");

/**
 * sort를 활용한 풀이 O(nlogn)
 * @param {*} participant
 * @param {*} completion
 */
function solution(participant, completion) {
  const sortedParticipant = participant.sort();
  const sortedCompletion = completion.sort();

  for (let i = 0; i < sortedParticipant.length; i++) {
    if (sortedParticipant[i] === sortedCompletion[i]) continue;
    return sortedParticipant[i];
  }
}

/**
 * map 를  활용한 풀이 O(n)
 * @param {*} participant
 * @param {*} completion
 */
function solution1(participant, completion) {
  const map = new Map();
  //참가자 명단 map 저장 {이름: 이름 등장 횟수}
  for (const p of participant) {
    map.set(p, (map.get(p) || 0) + 1);
  }
  //완주자 명단 map에서 제거
  for (const c of completion) {
    map.set(c, map.get(c) - 1);
    if (map.get(c) === 0) map.delete(c);
  }

  return [...map][0][0];
}
// asserts(solution(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo");
// asserts(
//   solution(
//     ["marina", "josipa", "nikola", "vinko", "filipa"],
//     ["josipa", "filipa", "marina", "nikola"]
//   ),
//   "vinko"
// );
// asserts(
//   solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]),
//   "mislav"
// );
asserts(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo");
asserts(
  solution1(
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["josipa", "filipa", "marina", "nikola"]
  ),
  "vinko"
);
asserts(
  solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]),
  "mislav"
);
