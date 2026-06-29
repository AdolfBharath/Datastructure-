class Node: #node creating 
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class bst:
  def __init__(self): # defining root as null by default
    self.root = None
  def insert(self,root,data):
    if root is None:
      return Node(data)
    if root<root.data:
      root.left = self.insert(root.left,data)
    elif root>root.data:
      root.right = self.insert(root.right,data)
    return root
  def inorder(self,root):  #left root right
    if root:
      self.inorder(self.left)
      print(root.data,end="")
      self.inorder(self.right)
  def preorder(self,root):  #root left right
    if root:
      print(root.data,end="")
      self.preorder(self.left)
      self.preorder(self.right)
  def postorder(self,root): #left right root
    if root:
      self.postorder(self.left)
      self.postorder(self.right)
      print(root.data,end="")
  def search(self,root,key):
    if root is None:
      return False
    if root == key:
      return True
    if key < root.data:
      return self.search(root.left,key)
    return self.search(root.right,key)
  def minimum(self,data):'
    while root.left:
      root = root.left
    return root.left
  def maximum(self,data):
    while root.right:
      root = root.right
    return root.right
  def delete(self,root,key):
    if root is None:
      return root
    if key< root.data:
      root.left = self.delete(root.left,key)
    elif key> root.data:
      root.left = self.delete(root.left,key)
    else:
      if root.left is None and root.right is None:
        return None
      if root.left is None:
        return root.right
      if root.right is None:
        return root.left
      temp = root.right
      while temp.left:
        temp = temp.left
      root.data = temp.data
      root.right = self.delete(root.right,temp.data)
    return root
      
      
