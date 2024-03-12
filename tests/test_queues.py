import pytest

from algorithmic import queues


def test_queues():
    queue = queues.QueueWithStacks()
    queue.push(7)
    queue.push(10)

    assert len(queue) == 2

    assert queue.peek() == 7
    assert queue.pop() == 7

    assert len(queue) == 1


def test_animal_queue():
    shelter = queues.AnimalQueue()

    shelter.enqueue(queues.Dog(name='Dog1'))
    shelter.enqueue(queues.Cat(name='Cat1'))
    shelter.enqueue(queues.Cat(name='Cat2'))

    with pytest.raises(NotImplementedError):
        shelter.enqueue('Dog')

    animal = shelter.dequeueAny()
    assert isinstance(animal, queues.Dog)
    assert animal.name == 'Dog1'

    animal = shelter.dequeueAny()
    assert isinstance(animal, queues.Cat)
    assert animal.name == 'Cat1'

    animal = shelter.dequeueAny()
    assert isinstance(animal, queues.Cat)
    assert animal.name == 'Cat2'

    shelter.enqueue(queues.Dog(name='Dog1'))
    animal = shelter.dequeueAny()
    assert isinstance(animal, queues.Dog)
    assert animal.name == 'Dog1'

    with pytest.raises(queues.AnimalQueueError):
        animal = shelter.dequeueAny()

    shelter.enqueue(queues.Dog(name='Dog1'))
    shelter.enqueue(queues.Cat(name='Cat1'))
    shelter.enqueue(queues.Cat(name='Cat2'))

    animal = shelter.dequeue_cat()
    assert isinstance(animal, queues.Cat)
    assert animal.name == 'Cat1'

    animal = shelter.dequeue_dog()
    assert isinstance(animal, queues.Dog)
    assert animal.name == 'Dog1'
