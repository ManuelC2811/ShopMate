class TreeNode:

  def __init__(self, key, product):
    self.key = key
    self.product = product
    self.left = None
    self.right = None
    self.height = 1


class AVLTree:

  def __init__(self):
    self.root = None

  def _height(self, node):
    if node is None:
      return 0
    return node.height

  def _balance(self, node):
    if node is None:
      return 0
    return self._height(node.left) - self._height(node.right)

  def _update_height(self, node):
    if node is not None:
      node.height = 1 + max(self._height(node.left), self._height(node.right))

  def _rotate_left(self, x):
    y = x.right
    x.right = y.left
    y.left = x
    self._update_height(x)
    self._update_height(y)
    return y

  def _rotate_right(self, y):
    x = y.left
    y.left = x.right
    x.right = y
    self._update_height(y)
    self._update_height(x)
    return x

  def _rebalance(self, node):
    if node is None:
      return node

    node.height = 1 + max(self._height(node.left), self._height(node.right))

    balance = self._balance(node)

    if balance > 1:
      if self._balance(node.left) < 0:
        node.left = self._rotate_left(node.left)
      return self._rotate_right(node)

    if balance < -1:
      if self._balance(node.right) > 0:
        node.right = self._rotate_right(node.right)
      return self._rotate_left(node)

    return node

  def insert(self, root, key, product):
    if root is None:
      return TreeNode(key, product)
    if key < root.key:
      root.left = self.insert(root.left, key, product)
    else:
      root.right = self.insert(root.right, key, product)

    return self._rebalance(root)

  def insert_key(self, key, product):
    self.root = self.insert(self.root, key, product)

  def _find_min(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def delete(self, root, key):
    if root is None:
      return root

    if key < root.key:
      root.left = self.delete(root.left, key)
    elif key > root.key:
      root.right = self.delete(root.right, key)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      root.key = self._find_min(root.right).key
      root.right = self.delete(root.right, root.key)

    return self._rebalance(root)

  def delete_key(self, key):
    self.root = self.delete(self.root, key)

  def search(self, root, key):
    if root is None:
      return False
    if key == root.key:
      return True
    elif key < root.key:
      return self.search(root.left, key)
    else:
      return self.search(root.right, key)

  def search_key(self, key):
    node = self.search(self.root, key)
    return node if node else None

  def inorder_traversal(self, root):
    if root is not None:
      self.inorder_traversal(root.left)
      print(root.key, end=' ')
      self.inorder_traversal(root.right)

  def display(self):
    self.inorder_traversal(self.root)
    print()
