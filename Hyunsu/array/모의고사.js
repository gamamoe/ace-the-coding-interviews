const assert = require("assert");
function solution(answers) {
  // 풀고보니 좋지 않은 자료구조인것 같음. sort를 하기 위해 object에서 다시 array로 바꿔 줘야 하고 굳이 object를 쓸 필요가 없어 보임.
  const students = {
    1: {
      pattern: [1, 2, 3, 4, 5],
      result: 0,
    },
    2: {
      pattern: [2, 1, 2, 3, 2, 4, 2, 5],
      result: 0,
    },

    3: {
      pattern: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
      result: 0,
    },
  };

  for (let i = 0; i < answers.length; i++) {
    Object.keys(students).forEach((studentNum) => {
      students[studentNum].result += addResult(
        isCorrect(students[studentNum].pattern, answers, i)
      );
    });
  }

  const sortedStudents = Object.entries(students).sort(
    (a, b) => a[1].result - b[1].result
  );
  const max = sortedStudents[sortedStudents.length - 1][1].result;
  const answer = sortedStudents
    .filter(([key, value]) => value.result === max)
    .map(([key, value]) => Number(key));

  return answer;
}

/**
 * improved version.
 * - object자료구조보다 array자료구조로 변경
 * - 인덱스를 studentId로 이용하여 접근하는 방법이 object보다 다루기가 쉬웠음.
 * - 코드 실행결과 tc 11번  (실행시간 8.3ms -> 6.22ms), 데이터 크기가 그렇게 크지 않아 유의미한 차이는 아닌것 같음.
 *
 * @param {*} answers
 * @param {*} questionNum
 * @returns [] 문제를 가장 많이 맞춘 학생의 번호 배열, 여러명일 경우 오름차순 정렬
 */

function solution1(answers) {
  const answer = [];
  const studentPatterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  const studentTestResult = Array(studentPatterns.length).fill(0); // [0번째 학생 맞춘 개수, 1번째 학생 맞춘개수, 2번째학생 맞춘개수]
  let max = Number.MIN_SAFE_INTEGER;
  //구해야 하는것: 문제를 가장 많이 맞춘
  //O(answers.length * studentPatterns.length) - 10000*3 = O(30000)
  for (let i = 0; i < answers.length; i++) {
    //정답들를 하나씩 돌면서
    // 각 학생의 패턴의 인덱스에 해당하는 값이 정답과 일치하는지 확인
    // 일치하면, 해당 학생의 맞춘 개수 증가
    studentPatterns.forEach((pattern, studentId) => {
      if (isCorrect(pattern, answers, i)) {
        studentTestResult[studentId] += 1;
        if (max < studentTestResult[studentId]) {
        }
        max = Math.max(max, studentTestResult[studentId]);
      }
    });
  }
  //O(3) max와 같은 중복된 studentId찾기
  for (const studentId in studentTestResult) {
    if (studentTestResult[studentId] === max) {
      answer.push(Number(studentId) + 1);
    }
  }

  return answer;
}
function isCorrect(pattern, answers, questionNum) {
  return pattern[questionNum % pattern.length] === answers[questionNum];
}

function addResult(isCorrect) {
  return isCorrect ? 1 : 0;
}

//test solution1
assert.deepEqual(solution1([1, 2, 3, 4, 5]), [1]);
assert.deepEqual(solution1([1, 3, 2, 4, 2]), [1, 2, 3]);
assert.deepEqual(solution1([1, 3, 2, 4, 2, 1, 2, 3, 4, 5, 1, 2]), [1]);

//test solution
assert.deepEqual(solution([1, 2, 3, 4, 5]), [1]);
assert.deepEqual(solution([1, 3, 2, 4, 2]), [1, 2, 3]);
assert.deepEqual(solution([1, 3, 2, 4, 2, 1, 2, 3, 4, 5, 1, 2]), [1]);
