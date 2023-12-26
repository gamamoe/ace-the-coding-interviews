/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * level = 트리의 depth
 * queue를 이용했을 때 queue에서 나온 노드의 인접 노드(차일드) 를 구하기가 편함.
 * 여기서 중요한것은 level을 어떤게 구별하느냐 인데,
 * 인접 노드를 큐에 넣을 때 레벨정보를 같이 넣음으로써 각 노드의 레벨을 트래킹.
 *
 * The number of nodes in the tree is in the range [0, 2000]
 * TimeComplexity : 노드 수는 최대 2000 이므로 O(n^2) shift()가능
 * 대신 dequeue를 사용하게 되면 O(n)까지 최적화 가능.
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  let result = [];
  let queue = [{ node: root, level: 0 }];
  while (queue.length) {
    //queue가 있으면 꺼내기
    const { node, level } = queue.shift();

    if (!node) continue;
    if (node.val != undefined && !result[level]) {
      result[level] = [node.val];
    } else if (node.val != undefined && result[level]) {
      result[level].push(node.val);
    }

    if (node.left) {
      queue.push({ node: node.left, level: level + 1 });
    }
    if (node.right) {
      queue.push({ node: node.right, level: level + 1 });
    }
  }

  return result;
};
