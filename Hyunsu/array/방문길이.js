const assert = require("assert");

/**
 
tc : 8~ 실패 
이유: 도착지점과, direction의 반대방향만 고려해서는 안된다. 
출발지점과 도착지점의 반대방향을 고려해야 한다.  
예) 5,5-> 4,5(북) 4,5->5,5 (남)인 경우 도착지점만 고려하게 되면, 4,5 와 5,5 를 비교하게 되므로 다른 경로로 판단하게 됨
 */

function solution(dirs) {
  let count = 0;
  const visited = Array.from({ length: 11 }, () => Array(11).fill(""));

  const dx = [-1, 0, 1, 0]; //북동남서
  const dy = [0, 1, 0, -1];
  const direction = { U: 0, R: 1, D: 2, L: 3 };

  let current = [5, 5];

  for (const dir of dirs) {
    const index = direction[dir];

    const nx = current[0] + dx[index];
    const ny = current[1] + dy[index];

    if (nx < 0 || ny < 0 || nx > 10 || ny > 10) continue;

    //check if visited
    const visitedX = nx;
    const visitedY = ny;
    current = [nx, ny];

    if (!visited[visitedX][visitedY]) {
      visited[visitedX][visitedY] = dir;
      count += 1;
      continue;
    }
    if (dir === visited[visitedX][visitedY]) {
      continue;
    }
    if (dir === getOppositeDir(visited[visitedX][visitedY], direction)) {
      continue;
    }

    visited[visitedX][visitedY] = dir;
    count += 1;
  }
  return count;
}

function getOppositeDir(dirChar, direction) {
  const directionList = Object.keys(direction); //["U","R","D","L"]
  for (let index in directionList) {
    if (index == direction[dirChar] + 2) {
      return directionList[index];
    }
    if (index == direction[dirChar] - 2) {
      return directionList[index];
    }
  }
}

/**
 * ver2.
 * 출발지점과 도착지점의 반대방향을 고려한 코드
 * 구하고자 하는것 : 처음 지나간 path의 수
 * 지나간 path를 set에 저장 하고 저장형태는 현재 좌표->다음좌표, 다음좌표->현재좌표를 set에 저장 (양방향으로 저장)
 * 현재 좌표-> 다음 좌표 (path)가 set에 존재한다면, continue
 * set에 존재하지 않는다면, 처음지나간 path이므로, set에 저장하고, count +=1
 * timeComplexity : O(n)
 * @param {*} dirs
 *
 */
function solution1(dirs) {
  let count = 0;
  let set = new Set();
  const dx = [-1, 0, 1, 0]; //북동남서
  const dy = [0, 1, 0, -1];
  const direction = { U: 0, R: 1, D: 2, L: 3 };

  let current = [5, 5];

  for (const dir of dirs) {
    const index = direction[dir];
    const [currentX, currentY] = current;
    const nx = current[0] + dx[index];
    const ny = current[1] + dy[index];

    if (nx < 0 || ny < 0 || nx > 10 || ny > 10) continue;

    //set에 현재 좌표->다음 좌표, 다음좌표->현재좌표를 문자열로 저장 (양방향으로 저장) 5554, 5455
    if (!set.has(`${currentX}${currentY}${nx}${ny}`)) {
      set.add(`${currentX}${currentY}${nx}${ny}`);
      set.add(`${nx}${ny}${currentX}${currentY}`);
      count += 1; // 처음 지나간 path이므로, count +=1
      current = [nx, ny]; // current 좌표 갱신
      continue;
    }
    current = [nx, ny];
  }

  return count;
}
//test
assert.equal(solution1("ULURRDLLU"), 7);
assert.equal(solution1("LULLLLLLU"), 7);
assert.equal(solution1("UDLR"), 2); //hidden case
assert.equal(solution1("UDLRDURL"), 4); //hidden case

// assert.equal(getOppositeDir("D", { U: 0, R: 1, D: 2, L: 3 }), "U");
