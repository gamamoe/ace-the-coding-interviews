/**
 * 첫번째 인수 lst를 이용하여 이진 탐색트리를 생성,
 * 두번째 search_list에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여 True혹은  False를 담은 리스트 result를 반환하는 함수
 *
 */
const assert = require("assert");
class Node {
  constructor(val, left, right) {
    this.val = val || 0;
    this.left = left || null;
    this.right = right | null;
  }
}

class BST {
  constructor(root) {
    this.root = root || null;
  }
  insert(value) {
    if (!value) throw "no value";
    let current, parent;
    if (!this.root) {
      this.root = new Node(value);
      return;
    }
    current = this.root;
    //current가 없을 때까지 traverse한다.
    while (current) {
      parent = current; //마지막 노드 지점 저장
      if (value < current.val) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    //current가 없는 지점에, node를 생성
    if (value < parent.val) {
      parent.left = new Node(value);
    } else {
      parent.right = new Node(value);
    }
  }

  find(value) {
    if (!value) throw "no value";
    if (!this.root) throw "no root node";
    //value 비교
    let current = this.root;
    while (current) {
      if (current.val === value) return true;
      current = value < current.val ? current.left : current.right;
    }
    return false;
  }
}
function solution(lst, search_list) {
  const bst = new BST();
  console.log("bst", bst);
  lst.forEach((v) => bst.insert(v));
  return search_list.map((v) => bst.find(v));
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
