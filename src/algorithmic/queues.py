from typing import Any
from algorithmic.stacks import Stack


class Queue:
    """Represents Queue data structure. """
    def __init__(self) -> None:
        self._s1 = Stack()
        self._s2 = Stack()

    def __len__(self):
        return len(self._s1)

    def push(self, data: Any) -> None:
        """Adds data to the Queue."""
        self._s1.push(data)

    def peek(self) -> Any:
        """Returns first inserted element of the Queue.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        self._s1_to_s2()
        data = self._s2.peek()
        self._s2_to_s1()

        return data

    def pop(self) -> Any:
        """Removes first inserted element of the Queue.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        self._s1_to_s2()
        data = self._s2.pop()
        self._s2_to_s1()

        return data

    def _s1_to_s2(self) -> None:
        while not self._s1.is_empty():
            self._s2.push(self._s1.pop())

    def _s2_to_s1(self) -> None:
        while not self._s2.is_empty():
            self._s1.push(self._s2.pop())
