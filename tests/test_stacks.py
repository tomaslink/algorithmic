import pytest

from algorithmic import stacks


def test_stack():
    assert repr(stacks.Node(3)) == '3'

    stack = stacks.Stack(capacity=2)
    stack.push(7)
    stack.push(10)

    with pytest.raises(stacks.FullStackError):
        stack.push(11)

    assert stack.pop() == 10
    assert stack.peek() == 7
    assert stack.pop() == 7

    with pytest.raises(stacks.EmptyStackError):
        stack.pop()

    with pytest.raises(stacks.EmptyStackError):
        stack.peek()

    stack = stacks.Stack(capacity=3)
    stack.push(7)
    stack.push(10)
    stack.push(12)

    assert len(stack) == 3

    bottom = stack.pop_bottom()

    assert bottom == 7
    assert len(stack) == 2


def test_stack_sort():
    stack = stacks.Stack(capacity=10)

    items = [7, 10, 44, 9, 3, 20]

    for it in items:
        stack.push(it)

    assert len(stack) == 6

    assert stack.peek() == 20
    assert stack.tolist() == items

    stack.sort()

    sorted_items = list(reversed(sorted(items)))
    for it in sorted_items:
        assert stack.pop() == it


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
    with pytest.raises(stacks.EmptyStackError):
        stack.min()


def test_set_of_stacks():
    setofstacks = stacks.SetOfStacks()
    maximum = setofstacks.stack_capacity

    with pytest.raises(stacks.EmptyStackError):
        setofstacks.pop()

    items = [1, 5, 2, 6]
    for data in items:
        setofstacks.push(data)

    assert len(setofstacks.stacks) == (len(items) // maximum)

    for stack in setofstacks.stacks:
        assert len(stack) <= setofstacks.stack_capacity

    assert setofstacks.pop() == 6
    assert setofstacks.pop() == 2

    assert len(setofstacks.stacks) == (len(items) // maximum) - (maximum // 2)

    assert setofstacks.pop() == 5
    assert setofstacks.pop() == 1

    with pytest.raises(stacks.EmptyStackError):
        setofstacks.pop()

    items = [1, 5, 2, 6]
    for data in items:
        setofstacks.push(data)

    assert len(setofstacks.stacks) == 2

    with pytest.raises(stacks.StackException):
        setofstacks.pop_at(4)

    assert setofstacks.pop_at(1) == 6
    assert len(setofstacks.stacks) == 2
    assert setofstacks.pop() == 2

    assert setofstacks.pop_at(0) == 5
    assert setofstacks.pop() == 1

    for data in items:
        setofstacks.push(data)

    assert repr(setofstacks) == (
        "1 -> 5 -> None" + "\n"
        "2 -> 6 -> None" + "\n"
    )

    assert len(setofstacks) == 4
    assert setofstacks.pop_at(0) == 5
    assert len(setofstacks.stacks[0]) == 2
