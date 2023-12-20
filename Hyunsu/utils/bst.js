const { Node } = require("./node");
class BST {
  constructor(root) {
    this.root = root || null;
  }

  insert(value) {
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
module.exports = { BST };
