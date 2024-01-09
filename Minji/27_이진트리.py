class Node:
	def __init__(self, item):
		self.left = None
		self.right = None
		self.item = item
  
class BinaryTree:
  def __init__(self):
    self.root = None
    
  def insert(self, key):
    self.root = self._insert(self.root, key)
      
  def _insert(self, root, key):
    if root is None:
      return Node(key)
    
    if key < root.item:
      root.left = self._insert(root.left, key)
    else:
      root.right = self._insert(root.right, key)
    
    return root
  
  def search(self, root, value):
    if root is None or root.item == value:
      return root is not None
    
    if value < root.item:
      return self.search(root.left, value)
    else:
      return self.search(root.right, value)

def solution(lst, search_lst):
  tree = BinaryTree()
  for value in lst:
    tree.insert(value)
  
  result = [tree.search(tree.root, value) for value in search_lst]
  return result