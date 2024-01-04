/**
 * 길찾기 게임
 * 1. 트리 생성
 * 2. 정렬 하기 - y 값 기준으로 내림차순 정렬
 * 3. 적절한 위치에 노드 삽입
 *
 *
 * @param {*} nodeinfo
 * @returns
 */
function solution(nodeinfo) {
  //generate tree
  //1, nodeinfo 의 인덱스와 함께 저장. ->[ [x,y], index]]
  const queue = nodeinfo.map((node, i) => [node, i + 1]);

  // 2. 정렬하기
  queue.sort((a, b) => b[0][1] - a[0][1]);

  const root = new Node(queue[0]);

  queue.slice(1).forEach((node, i) => {
    const [coor, index] = node;
    const [x, y] = coor;
    let rootNode = root;
    while (rootNode) {
      //x값 비교
      if (x > rootNode.value[0][0]) {
        if (rootNode.right) {
          //right child가 있으면, next노드 갱신
          rootNode = rootNode.right;
        } else {
          // right child가 없으면 노드 생성
          rootNode.right = new Node(node);
          break;
        }
      } else {
        if (rootNode.left) {
          rootNode = rootNode.left;
        } else {
          rootNode.left = new Node(node);
          break;
        }
      }
    }
  });

  const inorderArr = inorder(root, []);
  const postorderArr = postorder(root, []);
  return [inorderArr, postorderArr];
}

function inorder(root, visitOrder) {
  if (!root) return;

  visitOrder.push(root.value[1]);
  inorder(root.left, visitOrder);
  inorder(root.right, visitOrder);
  return visitOrder;
}

function postorder(root, visitOrder) {
  if (!root) return;
  postorder(root.left, visitOrder);
  postorder(root.right, visitOrder);
  visitOrder.push(root.value[1]);
  return visitOrder;
}

class Node {
  constructor(value) {
    this.value = value || [];
    this.left = null;
    this.right = null;
  }
}
