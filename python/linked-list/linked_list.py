from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    previous: Node = None
    succeeding: Node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._curr_iter_node = None

    def __len__(self):
        node_count = 0
        for _ in self:
            node_count += 1
        return node_count

    def __iter__(self):
        self._curr_iter_node = self.head
        return self

    def __next__(self):
        if self._curr_iter_node:
            node = self._curr_iter_node
            self._curr_iter_node = self._curr_iter_node.succeeding
            return node
        raise StopIteration

    def push(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.succeeding:
                curr = curr.succeeding
            node = Node(value, previous=curr)
            curr.succeeding = node
        return self.head

    def pop(self):
        if not self.head:
            raise IndexError("List is empty")
        curr = self.head
        while curr.succeeding:
            curr = curr.succeeding
        value = curr.value
        if curr == self.head:
            self.head = None
        else:
            curr.previous.succeeding = None
            curr.previous = None
        return value

    def shift(self):
        if not self.head:
            raise IndexError("List is empty")
        value = self.head.value
        if self.head.succeeding:
            new_head = self.head.succeeding
            new_head.previous = None
            self.head.succeeding = None
            self.head = new_head
        else:
            self.head = None
        return value

    def unshift(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = Node(value, succeeding=self.head)
            self.head.previous = node
            self.head = node
        return self.head

    def delete(self, value):
        if not self.head:
            raise ValueError("Value not found")
        if self.head.value == value:
            self.shift()
            return self.head
        node = self.head.succeeding
        while node:
            if node.value == value:
                node.previous.succeeding = node.succeeding
                if node.succeeding:
                    node.succeeding.previous = node.previous
                return self.head
            node = node.succeeding
        raise ValueError("Value not found")
