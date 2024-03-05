import pytest

from algorithmic import llists


def test_linked_list():
    llist = llists.LinkedList()
    assert llist.get_node("a") is None

    items1 = ["a", "b"]
    items2 = ["c", "d", "e", "e"]

    llist = llists.LinkedList(items1)
    assert repr(llist) == "a -> b -> None"
    assert llist.tostring() == "ab"
    assert len(llist) == 2

    llist.add_last(items2)
    assert llist.tolist() == items1 + items2

    assert repr(llist.head) == "a"

    one = llists.LinkedList(items2)
    two = llists.LinkedList(items2)
    assert one == two

    two.add_last(items1)
    assert not one == two

    with pytest.raises(ValueError):
        assert one == "string"


def test_remove_duplicates():
    items = ["a", "b", "b", "c", "d", "e", "e"]
    llist = llists.LinkedList(items)

    assert llist.tolist() == items

    llists.remove_duplicates(llist)
    assert llist.tolist() == list(dict.fromkeys(items))


def test_kth_to_last():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    ktolast = llists.kth_to_last(llist, k=1, size=len(items))
    assert ktolast.data == "e"

    ktolast = llists.kth_to_last(llist, k=3, size=len(items))
    assert ktolast.data == "c"

    with pytest.raises(ValueError):
        ktolast = llists.kth_to_last(llist, k=3, size=10)

    ktolast = llists.kth_to_last(llist, k=3)
    assert ktolast.data == "c"

    with pytest.raises(ValueError):
        ktolast = llists.kth_to_last(llist, k=10)


def test_kth_to_last_recursive():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    ktolast, i = llists.kth_to_last_recursive(llist.head, k=1)
    assert i == len(items)
    assert ktolast.data == "e"

    ktolast, i = llists.kth_to_last_recursive(llist.head, k=3)
    assert i == len(items)
    assert ktolast.data == "c"


def test_delete_node():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    node = llist.get_node("c")

    llists.delete_middle_node(node)
    assert llist.tolist() == ["a", "b", "d", "e"]

    with pytest.raises(ValueError):
        node = llist.get_node("e")
        llists.delete_middle_node(node)


def test_partition():
    items = [3, 5, 8, 5, 10, 2, 1]
    llist = llists.LinkedList(items)

    llist = llists.partition(llist, x=5)
    output = [1, 2, 3, 5, 8, 5, 10]
    assert llist.tolist() == output

    items = [6, 5, 3, 4, 10, 2, 9]
    llist = llists.LinkedList(items)
    llist = llists.partition(llist, x=5)
    output = [2, 4, 3, 6, 5, 10, 9]
    assert llist.tolist() == output


def test_sum():
    items1 = [7]
    items2 = [5]
    l1 = llists.LinkedList(items1)
    l2 = llists.LinkedList(items2)
    l3 = llists.sum(l1, l2)

    assert l3.tolist()[::-1] == [1, 2]

    items1 = [7, 1, 6]
    items2 = [5, 9, 2]
    l1 = llists.LinkedList(items1)
    l2 = llists.LinkedList(items2)
    l3 = llists.sum(l1, l2)

    assert l3.tolist()[::-1] == [9, 1, 2]


def test_palindrome():
    methods = ['reverse', 'iterative', 'recursive']

    with pytest.raises(ValueError):
        assert llists.is_palindrome("dummy", method='invalid')

    items = ["t", "a", "c", "o", "c", "a", "t"]
    llist = llists.LinkedList(items)
    for method in methods:
        assert llists.is_palindrome(llist, method=method)

    items = ["t", "a", "c", "o", "c", "a"]
    llist = llists.LinkedList(items)
    for method in methods:
        assert not llists.is_palindrome(llist, method=method)

    items = [0, 1, 2, 3, 2, 1, 0]
    llist = llists.LinkedList(items)
    for method in methods:
        assert llists.is_palindrome(llist, method=method)
