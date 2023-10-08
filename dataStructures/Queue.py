from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item: T):
        if self.is_full():
            raise Exception("La fila esta llena")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception("La fila esta vacia")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def get_front(self) -> T:
        if self.is_empty():
            raise Exception("La fila esta vacia")
        else:
            return self.queue[self.front]

    def get_rear(self) -> T:
      if self.is_empty():
        raise Exception("La Fila esta vacia")
      else:
        return self.queue[self.rear]

    def __str__(self) -> str:
        result = "Queue: "
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            result += str(self.queue[idx])
            if i < self.size - 1:
                result += ", "
        return result