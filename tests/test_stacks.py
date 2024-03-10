import pytest

from algorithmic import stacks


def test_stack():

    assert repr(stacks.Node(3)) == '3'

    stack = stacks.Stack()
    stack.push(7)
    stack.push(10)

    assert stack.pop() == 10
    assert stack.peek() == 7
    assert stack.pop() == 7

    with pytest.raises(stacks.EmptyStackException):
        stack.pop()

    with pytest.raises(stacks.EmptyStackException):
        stack.peek()


def test_stack_min():
    stack = stacks.StackMin()
    stack.push(7)
    stack.push(3)
    stack.push(5)

    assert stack.min() == 3

    stack.pop()
    assert stack.min() == 3

    stack.pop()
    assert stack.min() == 7

    stack.pop()
    with pytest.raises(stacks.EmptyStackException):
        stack.min()
