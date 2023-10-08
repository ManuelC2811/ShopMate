from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.stack: List[T] = [None] * size
        self.top = -1

    def push(self, item: T):
        if self.isFull():
            raise Exception("El stack está lleno")
        self.top += 1
        self.stack[self.top] = item

    def pop(self) -> T:
        if self.isEmpty():
            raise Exception("El stack está vacío")
        deleted = self.stack[self.top]
        self.top -= 1
        return deleted

    def top_element(self) -> T:
        if self.isEmpty():
            raise Exception("El stack está vacío")
        return self.stack[self.top]

    def isEmpty(self) -> bool:
        return self.top == -1

    def isFull(self) -> bool:
        return self.top == self.size - 1