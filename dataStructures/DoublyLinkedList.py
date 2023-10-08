class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 1

    def push_front(self, data):
        new_node = Node(data)
        if self.lenght == 0:
          self.head = new_node
          self.tail = new_node
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
        self.lenght +=1
      
      
    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
          self.tail = new_node
        else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node
        self.lenght += 1

    def pop_front(self):
        if self.head is None:
            print("La lista está vacía")
            return None
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        temp.next = None
        return temp.data

    def pop_back(self):
        if self.tail is None:
            print("La lista está vacía")
            return None
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        temp.prev = None
        return temp.data

    def add_after(self, prev_node, data):
        if prev_node is None:
            print("Error: El nodo previo no existe")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def add_before(self, given_node, data):
        if given_node is None:
            print("Error: El nodo dado no existe")
            return
        new_node = Node(data)
        new_node.prev = given_node.prev
        new_node.next = given_node
        if given_node.prev:
            given_node.prev.next = new_node
        given_node.prev = new_node
        if self.head == given_node:
            self.head = new_node

    def top_front(self):
        if self.head is None:
            raise Exception("La lista está vacía")
        return self.head.data

    def top_back(self):
        if self.tail is None:
            raise Exception("La lista está vacía")
        return self.tail.data

    def is_empty(self):
        return self.head is None

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                current.prev = None
                current.next = None
                return
            current = current.next

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
        while current:
            result.append(current.data)
            current = current.next
        return "\n".join(map(str, result))