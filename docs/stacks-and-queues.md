<h1 align="center" style="border-bottom: none;"> Stacks and Queues </h1>

[Stack Min]: ../src/algorithmic/stacks.py#L70
[Stack of Plates]: ../src/algorithmic/stacks.py#L187
[Queue via Stacks]: ../src/algorithmic/queues.py#L5
[Sort Stack]: ../src/algorithmic/stacks.py#L158
[Animal Shelter]: ../src/algorithmic/queues.py#L75


1. **[Stack Min]**: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

2. **[Stack of Plates]**: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
Implement also a function popAt(int index) which performs a pop operation on a specific sub-stack.


3. **[Queue via Stacks]**: Implement a Queue class which implements a queue using two stacks.


4. **[Sort Stack]**: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.


5. **[Animal Shelter]**: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeue_any, dequeue_dog,
and dequeue_cat. You may use the built-in deque data structure.]