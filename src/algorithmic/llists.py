from typing import List, Any


class Node:
    """Represents a node of a linked list.

    Args:
        data: the data to save in the node.
    """
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    """Represents a Linked List.

    Args:
        items: list of items to insert.
    """
    def __init__(self, items: List[Any] = None):
        self.head = None

        if items is not None:
            node = Node(data=items[0])
            self.head = node
            self.add_last(items[1:])

    def __repr__(self):
        items = self.tolist()
        items.append("None")

        return " -> ".join(items)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def tolist(self):
        """Converts linked list to list."""
        node = self.head
        items = []

        while node is not None:
            items.append(node.data)
            node = node.next

        return items

    def add_last(self, items: List[Any]):
        """Inserts list of items at the end of the linked list."""
        tail = self.head

        while tail.next is not None:
            tail = tail.next

        for item in items:
            tail.next = Node(data=item)
            tail = tail.next


def remove_duplicates(llist: LinkedList) -> None:
    """Removes duplicates (in-place) from a linked list.

    Complexity:
    - Time: O(N)
    - Space: O(N)

    Notes:
        If memory is important, an alternative with O(1) space can be implemented.
        In that case we can iterate the linked list with two runners (TODO).
        The time complexity in that case is O(N^2).
    """
    data = set()

    prev = llist.head
    for node in llist:
        if node.data in data:
            prev.next = node.next
            prev = node
            continue

        data.add(node.data)
        prev = node
