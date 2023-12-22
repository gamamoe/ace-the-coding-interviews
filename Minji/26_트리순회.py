def preorder(nodes, idx):
    res = []
    if idx < len(nodes):
      res.append(nodes[idx])
      res.extend(preorder(nodes, 2 * idx + 1 ))
      res.extend(preorder(nodes, 2 * idx + 2))
    return res

def inorder(nodes, idx):
  res = []
  if idx < len(nodes):
    res.extend(inorder(nodes, 2 * idx + 1))
    res.append(nodes[idx])
    res.extend(inorder(nodes, 2 * idx + 2))
  return res

def postorder(nodes, idx):
  res = []
  if idx < len(nodes):
    res.extend(postorder(nodes, 2 * idx + 1))
    res.extend(postorder(nodes, 2 * idx + 2))
    res.append(nodes[idx])
  return res

def solution(nodes):
  result = [
    preorder(nodes, 0),
    inorder(nodes, 0),
    postorder(nodes, 0)
  ]
  print("result : ", result)
  return result


nodes = [1, 2, 3, 4, 5, 6, 7]
solution(nodes)