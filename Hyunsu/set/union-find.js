const asserts = require("assert");
/**
 * 몸풀기 문제 : 간단한 유니온-파인드 알고리즘 구현
 * 초기 노드는 부모노드를 자신의 값으로 설정
 * UNION : 각 집합의 루트 노드를 기준으로 더 작은 노드를 더 큰 노드의 자식으로 연결
 * operations에 있는 연산을 모두 수행 후, 집합의 개수를 반환하는 solution함수 구현
 *
 * 1<= len(operations) <=100,000
 *
 * 시간복잡도는 O(n) 이하여야 함.
 * 집합의 개수는 부모노드와 자기자신의 노드와 같은 노드 개수.
 *
 */

function solution(k, operations) {
  const disjointSet = Array.from({ length: k }, (_, idx) => idx); // 초기 노드는 부모노드를 자신의 값으로 설정

  for (const operation of operations) {
    const [command, a, b] = operation;

    if (command === "u")
      union(find(a, disjointSet), find(b, disjointSet), disjointSet);
    else if (command === "f") find(a, disjointSet);
  }

  // 각 노드의 root노드를 찾아 집합 개수 구하기 : 대표 노드의 개수
  const set = new Set();
  disjointSet.forEach((parent) => set.add(find(parent, disjointSet)));

  return set.size;
}
// disjointSet[b] = a  a 노드의 대표노드는 b , O(1)
function union(a, b, disjointSet) {
  if (a !== b) disjointSet[b] = a;
}

// 경로 압축을 적용 하게 될 경우 : 평균 시간 복잡도 O(1)에 가까워짐
function find(a, parent) {
  if (parent[a] === a) return parent[a];
  return (parent[a] = find(parent[a], parent));
}

asserts.equal(
  solution(3, [
    ["u", 0, 1],
    ["u", 1, 2],
    ["f", 2],
  ]),
  1
);

asserts.equal(
  solution(4, [
    ["u", 0, 1],
    ["u", 2, 3],
    ["f", 0],
  ]),
  2
);
