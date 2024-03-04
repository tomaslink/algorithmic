from algorithmic import llists


def test_linked_list():
    _ = llists.LinkedList()

    items1 = ["a", "b"]
    items2 = ["c", "d", "e", "e"]

    llist = llists.LinkedList(items1)
    assert repr(llist) == "a -> b -> None"

    llist.add_last(items2)
    assert llist.tolist() == items1 + items2

    assert repr(llist.head) == "a"


def test_remove_duplicates():
    items = ["a", "b", "b", "c", "d", "e", "e"]
    llist = llists.LinkedList(items)

    assert llist.tolist() == items

    llists.remove_duplicates(llist)
    assert llist.tolist() == list(dict.fromkeys(items))
