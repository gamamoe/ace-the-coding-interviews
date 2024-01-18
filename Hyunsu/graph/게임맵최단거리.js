/**
 * 최단 거리 : BFS 사용
 * 1. 4방향 탐색
 * 2. visited 배열을 통해 방문 지점 까지의 거리를 업데이트 한다. (이전 노드의 거리 + 1)
 * 3. queue에는 방문할 노드를 넣는다.
 * 4. 방문할 노드가 없을때까지 반복한다.
 */
function solution(maps) {
  let n = maps[0].length;
  let m = maps.length;
  let x = 0,
    y = 0;
  let visited = Array.from({ length: maps.length }, () =>
    Array.from({ length: maps[0].length }, () => -1)
  );

  //북동남서
  const dx = [0, 1, 0, -1];
  const dy = [-1, 0, 1, 0]; //북 동 남 서
  let queue = [[y, x]];
  visited[y][x] = 1;

  while (queue.length) {
    const [y, x] = queue.shift();

    for (let i = 0; i < 4; i++) {
      let ny = dy[i] + y;
      let nx = dx[i] + x;
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 벗어나면 continue;
      if (maps[ny][nx] === 0) continue; // 벽이면 continue
      if (visited[ny][nx] !== -1) continue; //이미 방문한 노드면 continue
      queue.push([ny, nx]); //방문할 노드를 queue에 넣는다.
      visited[ny][nx] = visited[y][x] + 1; //방문처리시 이전 노드의 거리 +1
    }
  }
  return visited[m - 1][n - 1];
}

solution([
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1],
]);
