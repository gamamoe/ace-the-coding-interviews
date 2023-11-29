const assert = require("assert");

/**
 * !현재 코드는 미완성입니다. 테케에서 실패해서 조건을 맞추는 일을 반복하다보니 애초에 설계가 잘못된것 같아 재시도중.
 * 시도한 방법: sliding window
 * right가 ">" 를 만날 때까지 이동하고, ">" 를 만나면 right+1 값이 "<"인지 ">"인지에 따라 right++ or left++ 한다.
 * 현재 right인덱스+1 인덱스가 "<"라면 left를 옮겨서,
 * 짝수인지 확인하고, 짝수라면 pair가 될 수 있는지 확인한다.
 * pair가 될 수 있다면, maxSubString을 갱신
 *
 *
 * @param {*} S
 * @returns
 */
function solution(S) {
  const countGroup = {
    "<": 0,
    "?": 0,
    ">": 0,
  };
  let left = 0;
  let maxSubString = 0;

  for (let right = 0; right < S.length; right++) {
    //closing count가 <1 이면, continue를 하낟.
    countGroup[S[right]] += 1;

    if (countGroup[">"] < 1) continue;

    //closing count가 1이상이면,

    // 짝수인지 확인한다.
    if (isEven(getTotal(countGroup))) {
      // ?를 통해 pair가 될 수 있는지 확인
      if (isPaired(countGroup, getTotal(countGroup))) {
        //pair가 될 수 있는 경우
        // 개수 확인하여 maxSubString를 갱신한다.
        maxSubString = Math.max(maxSubString, right - left + 1);
      }
      //left를 옮긴다. only if (left가 <인 경우)
      if (S[right + 1] === "<") {
        left = right + 1;
        //countgroup 초기화
        countGroup["<"] = 0;
        countGroup["?"] = 0;
        countGroup[">"] = 0;
      }
    } else {
      // 짝수가 아니라면 두가지 선택 가능 ( right를 옮기거나 , left를 옮기거나 ) -> right를 해버리면, 현재 윈도우 내에서 짝수 && pair 되는 경우를 놓칠 수 있다.
      // 따라서, left를 옮긴다. only if (right+1 이  < 오픈 일 경우만 해당)
      if (S[right + 1] === ">") continue;
      left += 1;
    }
  }

  //right가 끝까지 왔음에도 > 이 없는경우
  if (countGroup[">"] < 1) {
    // 두가지의 상황

    if (isEven(getTotal(countGroup))) {
      if (isPaired(countGroup, getTotal(countGroup))) {
        maxSubString = Math.max(maxSubString, S.length - left);
      }
    } else {
      console.log("yes");
      //even이 아닐 경우, while문을 통해 짝수가 될 때까지 left를 옮긴다.
      //또는 수계산으로
      while (!isEven(getTotal(countGroup)) && left < S.length) {
        left += 1;
        countGroup[S[left]] -= 1;
        if (isPaired(countGroup, getTotal(countGroup))) {
          //pair가 될 수 있는 경우
          // 개수 확인하여 maxSubString를 갱신한다.
          maxSubString = Math.max(maxSubString, S.length - left);
        }
      }
    }
  }
  return maxSubString;
}

function getTotal(countGroup) {
  return countGroup["<"] + countGroup["?"] + countGroup[">"];
}

function isEven(num) {
  return num % 2 === 0;
}

function isPaired(countGroup, total) {
  const shouldAchieveCount = total / 2;
  const openAchievableCount = shouldAchieveCount - countGroup["<"];
  const closeAchievableCount = shouldAchieveCount - countGroup[">"];
  return openAchievableCount + closeAchievableCount === countGroup["?"];
}

// assert.equal(solution("<><??>>"), 4);
// assert.equal(solution("??????"), 6);
// assert.equal(solution("<<?"), 2);
assert.equal(solution(">>?"), 0);
// assert.equal(solution("<<<?><"), 4);
// assert.equal(solution("<<<?>>"), 4);
// assert.equal(solution("<>>??>>"));
// assert.equal(solution("<><<??>>"), 6);
