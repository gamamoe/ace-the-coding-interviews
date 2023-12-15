const asserts = require("asserts");

/**
 * 문제를 잘 읽자..
 * 익숙한 것에 너무나 당연하게 생각하고 넘어가지 말자
 * record의 두번째 인자인 uid를( uuid처럼) 항상 붙는 prefix라고 생각하고 uid의 네번째 인덱스부터 uid라고 생각함.
 *
 *
 * @param {*} record
 * @returns
 */

function solution(record) {
  let nameTable = {};
  let messages = [];
  const chatMessageTable = {
    Enter: "님이 들어왔습니다.",
    Leave: "님이 나갔습니다.",
  };

  for (const singleRecord of record) {
    let [action, uid, name] = singleRecord.split(" ");
    // uid = uid.split("").slice(3).join(""); ❌  uid는 항상 3번째 인덱스부터 시작한다고 생각하면 안된다.
    if (action === "Enter") {
      nameTable[uid] = name;
      messages.push({ uid, action: chatMessageTable[action] });
      continue;
    }
    if (action === "Leave") {
      messages.push({ uid, action: chatMessageTable[action] });
      continue;
    }
    if (action === "Change") {
      nameTable[uid] = name;
      continue;
    }
  }

  return messages.map(({ uid, action }) => `${nameTable[uid]}${action}`);
}

asserts.deepEqual(
  solution(["Enter uid1234 Muzi", "Leave uid1234", "Change uid1234 Prodo"]),
  ["Prodo님이 들어왔습니다.", "Prodo님이 나갔습니다."]
);

asserts.deepEqual(
  solution([
    "Enter uid1234 Muzi",
    "Leave uid1234",
    "Enter uid2345 Muzi",
    "Enter uid3456 Muzi",
    "Change uid1234 Prodo",
  ]),
  [
    "Prodo님이 들어왔습니다.",
    "Prodo님이 나갔습니다.",
    "Muzi님이 들어왔습니다.",
    "Muzi님이 들어왔습니다.",
  ]
);

asserts.deepEqual(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ]),
  [
    "Prodo님이 들어왔습니다.",
    "Ryan님이 들어왔습니다.",
    "Prodo님이 나갔습니다.",
    "Prodo님이 들어왔습니다.",
  ]
);
