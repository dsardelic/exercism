from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, value: int):
        self._value: int = value
        self._next: Node | None = None

    def value(self) -> int:
        return self._value

    def next(self) -> Node | None:
        return self._next

    def set_next(self, node) -> None:
        self._next = node


class LinkedList:
    def __init__(self, values: Optional[list[int]] = None):
        self._head = None
        self._curr_iter_node = None
        if values:
            for value in values:
                self.push(value)

    def __len__(self) -> int:
        ret_val = 0
        node = self._head
        while node:
            ret_val += 1
            node = node.next()
        return ret_val

    def __iter__(self) -> LinkedList:
        self._curr_iter_node = self._head
        return self

    def __next__(self) -> int:
        if self._curr_iter_node:
            iter_node = self._curr_iter_node
            self._curr_iter_node = self._curr_iter_node.next()
            return iter_node.value()
        raise StopIteration

    def head(self) -> Node | None:
        if self._head:
            return self._head
        raise EmptyListException("The list is empty.")

    def push(self, value: int) -> None:
        node = Node(value)
        node.set_next(self._head)
        self._head = node

    def pop(self) -> int:
        if not self._head:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = self._head.next()
        return node.value()

    def reversed(self: LinkedList) -> LinkedList:
        return LinkedList(list(self))


class EmptyListException(Exception):
    pass
