<h1 align="center" style="border-bottom: none;"> Linked Lists </h1>

[Remove duplicates]: ../src/algorithmic/llists.py#L68
[Return Kth to Last]: ../src/algorithmic/llists.py#L93
[Delete Middle Node]: ../src/algorithmic/llists.py#L163
[Partition]: ../src/algorithmic/llists.py#L177
[Sum Lists]: ../src/algorithmic/llists.py#L206
[Palindrome]: ../src/algorithmic/llists.py#L275
[Intersection]: ../src/algorithmic/llists.py#L370
[Loop Detection]: ../src/algorithmic/llists.py#L403


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

5. **[Sum Lists]**: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
    * **EXAMPLE**:
        - `Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295`.
        - `Output: 2 -> 1 -> 9. That is, 912`.

6. **[Palindrome]**: Implement a function to check if a linked list is a palindrome.

7. **[Intersection]**: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

8. **[Loop Detection]**: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop. A circular linked list is a corrupt linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
    * EXAMPLE
        - `Input: A -> B -> C -> D -> E -> C [the same C as earlier]`.
        - `Output: C`.