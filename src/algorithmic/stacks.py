from typing import Any, Tuple


class StackException(Exception):
    pass


class EmptyStackError(StackException):
    pass


class FullStackError(StackException):
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
    """Represents a Stack data structure.

    Args:
        capacity: maximum capacity allowed.
    """

    def __init__(self, capacity=10) -> None:
        self._top = None
        self._capacity = capacity
        self._current_capacity = 0

    def __len__(self) -> int:
        node = self._top
        i = 0

        while node is not None:
            i += 1
            node = node.next

        return i

    def __repr__(self):
        items = list(reversed(self.tolist()))
        items.append("None")

        return " -> ".join([str(i) for i in items])

    def tolist(self):
        """Converts stack to list.

        Complexity:
            - Time: O(N).
            - Space: O(N).
        """
        node = self._top
        items = []

        while node is not None:
            items.append(node.data)
            node = node.next

        return items

    def pop(self) -> Any:
        """Returns and removes the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        data = self._top.data
        self._top = self._top.next

        self._current_capacity -= 1

        return data

    def peek(self) -> Any:
        """Returns the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_empty():
            raise EmptyStackError()

        return self._top.data

    def push(self, data: Any) -> None:
        """Adds data to the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if self.is_full():
            raise FullStackError("This stack reached full capacity ({})".format(self._capacity))

        new_top = Node(data)
        new_top.next = self._top
        self._top = new_top

        self._current_capacity += 1

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return self._top is None

    def is_full(self) -> bool:
        """Checks if the stack is full."""
        return self._current_capacity == self._capacity

    def pop_bottom(self) -> Tuple[Any, Any]:
        """Pops the bottom of the stack.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        bottom = self._top
        size = len(self)

        def _pop_bottom(i):
            nonlocal bottom
            nonlocal self

            if self.is_empty():
                return

            node = self.pop()

            if i == size - 1:
                bottom = node

            _pop_bottom(i + 1)

            if i != size - 1:
                self.push(node)

        _pop_bottom(0)

        return bottom


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
            raise EmptyStackError()

        return self._top.substack_min


class SetOfStacks(Stack):
    """Implements a stack composed as a set of stacks of limited capacity.

    Args:
        stack_capacity: the max capacity of each stack.
    """
    DEFAULT_STACK_CAPACITY = 2

    def __init__(self, stack_capacity=DEFAULT_STACK_CAPACITY) -> None:
        self.stacks = []
        self.stack_capacity = stack_capacity

    def __len__(self) -> int:
        i = 0
        for stack in self.stacks:
            i += len(stack)

        return i

    def __repr__(self) -> str:
        res = ''
        for s in self.stacks:
            res += f'{repr(s)}\n'

        return res

    def push(self, data: Any) -> None:
        """Adds data to the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if not self.stacks or self.stacks[-1].is_full():
            self.stacks.append(Stack(self.stack_capacity))

        self.stacks[-1].push(data)

    def pop(self) -> Any:
        """Returns and removes the top of the stack.

        Complexity:
            - Time: O(1).
            - Space: O(1).
        """
        if not self.stacks:
            raise EmptyStackError()

        stack = self.stacks[-1]
        data = stack.pop()

        if stack.is_empty():
            self.stacks.pop()

        return data

    def pop_at(self, i: int) -> Any:
        """Returns and removes an item from the stack and index i.
        If stack at index i is an intermediate stack, shifts all subsequent stacks
            so that all the intermediate stacks are at full capacity and the order of insertion
                is preserved.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        try:
            stack_at_i = self.stacks[i]
        except IndexError:
            raise StackException(
                "Index {} out of bounds for length {}".format(i, len(self.stacks)))

        last_index = len(self.stacks) - 1
        data = stack_at_i.pop()

        j = i + 1
        while j <= last_index:
            bottom = self.stacks[j].pop_bottom()
            self.stacks[j - 1].push(bottom)
            j += 1

        return data
