class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def push_front(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    if self.tail is None:
      self.tail = self.head

  def push_back(self, data):
    new_node = Node(data)
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def pop_front(self):
    if self.head is None:
      print("La lista está vacía")
      return
    temp = self.head
    self.head = self.head.next
    temp.next = None
    return temp.data

  def pop_back(self):
    if self.head is None:
      print("La lista está vacía")
      return
    if self.head.next is None:
      data = self.head.data
      self.head = None
      self.tail = None
      return data
    prev = None
    current = self.head
    while current.next is not None:
      prev = current
      current = current.next
    data = current.data
    prev.next = None
    self.tail = prev
    return data

  def add_after(self, prev_node, data):
    if prev_node is None:
      print("Error")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def add_before(self, given_node, data):
    new_node = Node(data)
    if given_node == self.head:
      new_node.next = self.head
      self.head = new_node
    else:
      current = self.head
      while current is not None and current.next != given_node:
        current = current.next
      if current is None:
        print("No se encontró el nodo")
      else:
        new_node.next = given_node
        current.next = new_node

  def top_front(self):
    if self.head is None:
      raise Exception("La lista está vacía")
    else:
      return self.head.data

  def top_back(self):
    if self.head is None:
      raise Exception("La lista está vacía")
    else:
      return self.tail.data

  def is_empty(self):
    return self.head is None

  def delete(self, data):
    prev = None
    current = self.head
    if current is not None and current.data == data:
      self.head = self.head.next
      return
    while current is not None and current.data != data:
      prev = current
      current = current.next
    if current is None:
      return
    prev.next = current.next

  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next

  def __str__(self):
    current = self.head
    if current is None:
      return "La lista está vacía"
    result = []
    while current is not None:
      result.append(current.data)
      current = current.next
    return "\n".join(map(str, result))