class TreeNode:

  def __init__(self, product):
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

  def insert(self, root, product):
    if root is None:
      return TreeNode(product)
      
    if product.nombre < root.product.nombre:
      root.left = self.insert(root.left, product)
    elif product.nombre > root.product.nombre:
      root.right = self.insert(root.right, product)
    else:
      root.product.cantidad += product.cantidad

    return self._rebalance(root)

  def insert_product(self, product):
    self.root = self.insert(self.root, product)

  def _find_min(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def delete(self, root, name):
    if root is None:
      return root

    if name < root.product.nombre:
      root.left = self.delete(root.left, name)
    elif name > root.product.nombre:
      root.right = self.delete(root.right, name)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      root.product = self._find_min(root.right).product
      root.right = self.delete(root.right, root.product.nombre)

    return self._rebalance(root)

  def delete_product(self, name):
    if self.search_product(name) is not None:
      self.root = self.delete(self.root, name)
      print(f"{name} ha sido eliminado de la lista.")
    else:
      print(f"{name} no se encontro en la lista.")
    
  def search(self, root, name):
    if root is None:
      return None
    if name == root.product.nombre:
      return root
    elif name < root.product.nombre:
      return self.search(root.left, name)
    else:
      return self.search(root.right, name)

  def search_product(self, name):
    node = self.search(self.root, name)
    return node

  def inorder_traversal(self, root):
    if root is not None:
      self.inorder_traversal(root.left)
      print(root.product.name, end=' ')
      self.inorder_traversal(root.right)

  def display(self):
    self.inorder_traversal(self.root)
    print()