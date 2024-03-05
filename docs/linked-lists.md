<h1 align="center" style="border-bottom: none;"> Linked Lists </h1>

[Remove duplicates]: ../src/algorithmic/llists.py#L68
[Return Kth to Last]: ../src/algorithmic/llists.py#L93
[Delete Middle Node]: ../src/algorithmic/llists.py#L163
[Partition]: ../src/algorithmic/llists.py#L177


1. **[Remove duplicates]**: Write code to remove duplicates from an unsorted linked list. 
How would you solve this problem if a temporary buffer is not allowed?

2. **[Return Kth to Last]**: Implement an algorithm to find the kth to last element of a singly linked list.
[Iteratively](../src/algorithmic/llists.py#L93) and [recursively](../src/algorithmic/llists.py#L134). 

3. **[Delete Middle Node]**: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
    * **EXAMPLE**:
        - `Input: the node c from the linked list a -> b -> c -> d -> e -> f`.
        - `Output: nothing is returned, but the new linked list looks like a -> b-> d -> e -> f`.

4. **[Partition]**: Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list,
the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.
    * **EXAMPLE**:
        - `Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]`.
        - `Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8`.