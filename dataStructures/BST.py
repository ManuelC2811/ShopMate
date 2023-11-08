class Node:
  def __init__(self, product):
    self.product = product
    self.left = None
    self.right = None

class BST:

  def __init__(self):
    self.root = None
    
  def insert(self, product):
    if self.root is None:
        self.root = Node(product)
    else:
        self._insert_recursive(self.root, product)

  def _insert_recursive(self, node, product):
    if product.nombre < node.product.nombre:
        if node.left is None:
            node.left = Node(product)
        else:
            self._insert_recursive(node.left, product)
    else:
        if node.right is None:
            node.right = Node(product)
        else:
            self._insert_recursive(node.right, product)

  def search_product(self, root, name):
    if root is None:
      return None
    if name == root.product.nombre:
      return root
    elif name < root.product.nombre:
      return self.search_product(root.left, name)
    else:
      return self.search_product(root.right, name)

  def contains(self, name):
    node = self.search_product(self.root, name)
    return node

  def remove(self, value):
    if self.contains(value) is not None:
      self.root = self._remove_recursive(self.root, value)
      print(f"\n{value} ha sido eliminado\n")
    else:
      print(f"\n{value} no ha sido encontrado en la lista\n")

  def _remove_recursive(self, node, value):
    if node is None:
      return None
    if value < node.product.nombre:
      node.left = self._remove_recursive(node.left, value)
    elif value > node.product.nombre:
      node.right = self._remove_recursive(node.right, value)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      node.product = self._get_min_value(node.right)
      node.right = self._remove_recursive(node.right, node.product)
    return node

  def _get_min_value(self, node):
    while node.left is not None:
      node = node.left
    return node.product
