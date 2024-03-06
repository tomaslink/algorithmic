import copy
from typing import List, Any, Tuple


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
            self.add_items(items[1:])

    def __repr__(self):
        items = self.tolist()
        items.append("None")

        return " -> ".join([str(i) for i in items])

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        size, _ = self.size_and_tail()

        return size

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            raise ValueError("A LinkedList can only be compared to another LinkedList.")

        one = self.head
        two = other.head

        while one is not None and two is not None:
            if not one.data == two.data:
                return False

            one = one.next
            two = two.next

        return one is None and two is None

    def tolist(self):
        """Converts linked list to list."""
        node = self.head
        items = []

        while node is not None:
            items.append(node.data)
            node = node.next

        return items

    def tostring(self):
        return ''.join(map(str, self.tolist()))

    def add_node(self, node: Node):
        """Inserts a node at the end of the linked-list."""
        last_node = self.get_last()
        last_node.next = node

    def add_items(self, items: List[Any]):
        """Inserts list of items at the end of the linked list."""
        tail = self.head

        while tail.next is not None:
            tail = tail.next

        for item in items:
            tail.next = Node(data=item)
            tail = tail.next

    def get_node(self, data):
        """Returns the node with provided data. If more than one, first is returned."""
        node = None
        for n in self:
            if n.data == data:
                node = n
                break

        return node

    def get_last(self):
        """Returns last node."""
        node = None
        for n in self:
            node = n

        return node

    def at(self, idx):
        """Returns node at index idx."""
        i = 0
        for node in self:
            if i == idx:
                return node

            i += 1

        raise ValueError("index {} out of bounds for list: {}!".format(idx, self.tolist()))

    def reverse(self):
        """Reverses the linked list in-place.

        Complexity:
            - Time: O(N).
            - Space: O(1)
        """
        _prev = None
        _current = self.head

        while _current is not None:
            _next = _current.next
            _current.next = _prev
            _prev = _current
            _current = _next

        self.head = _prev

    def size_and_tail(self):
        """Returns the size and tail of linked-list."""
        i = 0
        node = None

        for n in self:
            node = n
            i += 1

        return i, node


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


def kth_to_last(llist: LinkedList, k: int, size: int = None) -> Node:
    """Returns the kth element, counting from the last.

    Time Complexity:
    - Time: O(N).
    - Space: O(1).

    """
    if size is not None:
        k = size - k

        i = 0
        k_node = None
        for node in llist:
            if i == k:
                k_node = node
            i += 1

        if k_node is None:
            raise ValueError("size parameter was greater than real size of linked list.")

        return k_node

    p1 = llist.head
    p2 = llist.head

    i = 0
    while i < k:
        p1 = p1.next
        if p1 is None:
            raise ValueError("k parameter was greater than the size of the linked list")

        i += 1

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2


def kth_to_last_recursive(head: Node, k: int) -> Tuple[Node, int]:
    """Returns the kth element, counting from the last, with a recursive approach.

    Time Complexity:
    - Time: O(N).
    - Space: O(N).
    """
    if head is None:
        return head, 0

    node, i = kth_to_last_recursive(head.next, k)

    i += 1
    if i == k:
        return head, i

    return node, i


def delete_middle_node(node: Node) -> None:
    """Deletes a middle node from a linked-list.

    Complexity:
        - Time: O(1).
        - Space: (1).
    """
    if node.next is None:
        raise ValueError("node is not a middle one!")

    node.data = node.next.data
    node.next = node.next.next


def partition(llist: LinkedList, x: int) -> LinkedList:
    """Partition a linked list around value x.

    Complexity:
    - Time: O(N).
    - Space: O(1).
    """

    head = llist.head
    node = head.next

    _prev = head
    while node is not None:
        _next = node.next

        if node.data < x:
            _prev.next = node.next
            node.next = head
            head = node
        else:
            _prev = node

        node = _next

    llist.head = head

    return llist


def sum(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """Sum of two numbers represented by linked lists.

    The algorithm assumes the numbers are represented in reversed order.

    Complexity:
        Time: O(N).
        Space: O(N).

    Where N is max(A, B), and A, B the lengths of l1 and l2, respectively.

    Returns:
        the sum represented as a linked-list.
    """
    l1_numbers = l1.tolist()[::-1]
    l2_numbers = l2.tolist()[::-1]

    l1_int = int(''.join(map(str, l1_numbers)))
    l2_int = int(''.join(map(str, l2_numbers)))

    l3_int = l1_int + l2_int

    l3_numbers = [int(x) for x in str(l3_int)]

    return LinkedList(l3_numbers[::-1])


def is_palindrome(llist: LinkedList, method: str = 'reverse') -> bool:
    """Checks if the items in a linked-list form a palindrome.

    Complexity:
        - Time: O(N).
        - Space: O(N).
    """
    METHODS = ['iterative', 'reverse', 'recursive']

    if method not in METHODS:
        raise ValueError("Method {} not valid. Choose from {}".format(method, METHODS))

    if method == 'reverse':
        llist_copy = copy.deepcopy(llist)
        llist.reverse()

        return llist_copy == llist

    elif method == 'iterative':
        stack = []
        p1 = llist.head
        p2 = llist.head

        while p1 is not None and p1.next is not None:
            stack.append(p2.data)
            p1 = p1.next.next
            p2 = p2.next

        if p1 is not None:  # odd number of elements. Delete middle one.
            p2 = p2.next

        while p2 is not None:
            if not p2.data == stack.pop():
                return False

            p2 = p2.next

        return True

    else:
        def recursive(head: Node, length: int):
            if head is None or length <= 0:
                return head, True

            if length == 1:
                return head.next, True

            node, is_palindrome = recursive(head.next, length - 2)

            if not is_palindrome or node is None:
                return node, is_palindrome

            return node.next, head.data == node.data

        _, res = recursive(llist.head, len(llist))

        return res


def intersection(l1: LinkedList, l2: LinkedList):
    """Finds an intersecting node between l2 and l2 linked-lists."""

    l1_len, l1_tail = l1.size_and_tail()
    l2_len, l2_tail = l2.size_and_tail()

    if l1_len == 0 or l2_len == 0:
        return False, None

    if l1_tail is not l2_tail:
        return False, None

    len_diff = abs(l1_len - l2_len)

    p1 = l1.head
    p2 = l2.head

    if l1_len > l2_len:
        p1 = l1.at(len_diff)

    if l2_len > l1_len:
        p2 = l2.at(len_diff)

    while p1 is not None:
        if p1 is p2:
            break

        p1 = p1.next
        p2 = p2.next

    return True, p1
