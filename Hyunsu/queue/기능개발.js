const assert = require("assert");

function solution(progresses, speeds) {
  const queues = [];
  const remainingDays = Array.from({ length: progresses.length }, (v, i) =>
    Math.ceil((100 - progresses[i]) / speeds[i])
  );

  //remainingDays 를 iterate하면서, queue에 넣기
  let queue = [];
  let dayForDeploy = 0;
  for (const day of remainingDays) {
    if (!queue.length) {
      queue.push(day);
      dayForDeploy = queue[0];
      continue;
    }
    //크면 같은날 배포 못함.
    if (day > dayForDeploy) {
      queues.push(queue);
      queue = [day];
      dayForDeploy = day;
    } else {
      queue.push(day);
    }
  }
  if (queue.length) {
    queues.push(queue);
  }
  return queues.map((queue) => queue.length);
}

assert.deepEqual(solution([93, 30, 55], [1, 30, 5]), [2, 1]);
assert.deepEqual(
  solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1]),
  [1, 3, 2]
);
assert.deepEqual(solution([99, 99, 99], [1, 1, 1]), [3]);
