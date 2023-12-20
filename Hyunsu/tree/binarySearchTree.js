/**
 * 첫번째 인수 lst를 이용하여 이진 탐색트리를 생성,
 * 두번째 search_list에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여 True혹은  False를 담은 리스트 result를 반환하는 함수
 *
 */
const assert = require("assert");
const { BST } = require("../utils/bst");
/**
 * Represents a Binary Search Tree.
 * insert 시 traverse 하여 적절한 자리를 찾아야 함. (이미 노드가 존재 한다면 다음 노드로 traverse 해야한다)
 * 적절한 노드의 기준은 parent노드의 값보다 작으면 parent.left, 그 외의 경우 parent.right로 지정
 *
 *
 * @class
 */

function solution(lst, search_list) {
  const bst = new BST();
  lst.forEach((v) => bst.insert);
  return search_list.map((v) => bst.find);
}

assert.deepEqual(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]), [
  true,
  true,
  true,
  false,
]);
assert.deepEqual(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]), [
  false,
  false,
  false,
  false,
  false,
]);
