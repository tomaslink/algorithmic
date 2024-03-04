<h1 align="center" style="border-bottom: none;"> Linked Lists </h1>

[Remove duplicates]: ../src/algorithmic/llists.py#L68
[Return Kth to Last]: ../src/algorithmic/llists.py#L93
[Delete Middle Node]: ../src/algorithmic/llists.py#L163


1. **[Remove duplicates]**: Write code to remove duplicates from an unsorted linked list. 
How would you solve this problem if a temporary buffer is not allowed?

2. **[Return Kth to Last]**: Implement an algorithm to find the kth to last element of a singly linked list.
[Iteratively](../src/algorithmic/llists.py#L93) and [recursively](../src/algorithmic/llists.py#L134). 

3: **[Delete Middle Node]**: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
    * **EXAMPLE**:
        - Input: the node c from the linked list a -> b -> c -> d -> e -> f.
        - Output: nothing is returned, but the new linked list looks like a -> b-> d -> e -> f.