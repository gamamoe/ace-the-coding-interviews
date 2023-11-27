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
function isCorrect(pattern, answer, questionNum) {
  return pattern[questionNum % pattern.length] === answer[questionNum];
}

function addResult(isCorrect) {
  return isCorrect ? 1 : 0;
}

assert.deepEqual(solution([1, 2, 3, 4, 5]), [1]);
assert.deepEqual(solution([1, 3, 2, 4, 2]), [1, 2, 3]);
assert.deepEqual(solution([1, 3, 2, 4, 2, 1, 2, 3, 4, 5, 1, 2]), [1]);
