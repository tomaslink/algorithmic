<h1 align="center" style="border-bottom: none;"> Stacks and Queues </h1>

[Stack Min]: ../src/algorithmic/stacks.py#L70
[Stack of Plates]: ../src/algorithmic/stacks.py#L187
[Queue via Stacks]: ../src/algorithmic/queues.py#L5


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