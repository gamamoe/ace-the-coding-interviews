/**
 * Map을 이용하여 left와 right에 토핑을 넣고 빼는 방식으로 접근.
 * 보완할점은 set을 이용하는 방법이 더 간결 할 것 같다.
 * Time Complexity : O(n)
 * @param {*} topping
 * @returns
 */
function solution(topping) {
  var answer = 0;
  let left = [];
  let right = [];
  const leftToppingMapper = new Map();
  const rightToppingMapper = new Map();
  // 초기 right에 모든 토핑을 넣고, 토핑의 개수를 센다
  topping.forEach((v) => {
    rightToppingMapper.set(v, (rightToppingMapper.get(v) || 0) + 1);
    right.push(v);
  });
  //주어진 토핑만큼 순회하면서 right에서 하나씩 pop 하여, left에 넣는다.
  // 순회는 right가 빌때까지 한다.
  while (right.length) {
    //left로 옮기기
    const last = right.pop();
    left.push(last);
    //left에 토핑을 추가 한다.
    leftToppingMapper.set(last, (leftToppingMapper.get(last) || 0) + 1);
    //right에서 토핑을 제거한다.
    rightToppingMapper.set(last, rightToppingMapper.get(last) - 1);
    //right에서 토핑을 제거할 때, 0 이 되면 map에서 제거한다.
    if (rightToppingMapper.get(last) === 0) {
      rightToppingMapper.delete(last);
    }
    // map에 저장된 keyd의 개수로 비교하여 같으면 answer를 증가시킨다.
    if (leftToppingMapper.size === rightToppingMapper.size) {
      answer += 1;
    }
  }
  return answer;
}
