from typing import Any


class EmptyStackException(Exception):
    pass


class Node:
    """Represents a node of a stack.

    Args:
        data: the data to save in the node.
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    """Represents a Stack data structure."""

    def __init__(self) -> None:
        self._top = None

    def pop(self) -> Any:
        """Returns and removes the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_empty():
            raise EmptyStackException()

        data = self._top.data
        self._top = self._top.next

        return data

    def peek(self) -> Any:
        """Returns the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_empty():
            raise EmptyStackException()

        return self._top.data

    def push(self, data: Any) -> None:
        """Adds data to the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        new_top = Node(data)
        new_top.next = self._top
        self._top = new_top

    def is_empty(self) -> bool:
        return self._top is None


class StackMin(Stack):
    """Implements a Stack with a min method that returns the minimum."""

    def push(self, data: Any) -> None:
        """Adds data to the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        new_top = Node(data)
        new_top.substack_min = data

        if not self.is_empty():
            if self._top.substack_min < new_top.substack_min:
                new_top.substack_min = self._top.substack_min

        new_top.next = self._top
        self._top = new_top

    def min(self) -> Any:
        """Returns the minimum of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_empty():
            raise EmptyStackException()

        return self._top.substack_min
