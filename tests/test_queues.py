from algorithmic import queues


def test_queues():
    queue = queues.Queue()
    queue.push(7)
    queue.push(10)

    assert len(queue) == 2

    assert queue.peek() == 7
    assert queue.pop() == 7

    assert len(queue) == 1
