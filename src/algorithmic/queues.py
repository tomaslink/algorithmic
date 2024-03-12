from typing import Any
from datetime import datetime
from collections import deque
from dataclasses import dataclass

from algorithmic.stacks import Stack


class QueueWithStacks:
    """Implements Queue data structure using two stacks. """
    def __init__(self) -> None:
        self._s1 = Stack()
        self._s2 = Stack()

    def __len__(self):
        return len(self._s1)

    def push(self, data: Any) -> None:
        """Adds data to the Queue."""
        self._s1.push(data)

    def peek(self) -> Any:
        """Returns first inserted element of the Queue.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        self._s1_to_s2()
        data = self._s2.peek()
        self._s2_to_s1()

        return data

    def pop(self) -> Any:
        """Removes first inserted element of the Queue.

        Complexity:
            - Time: O(N).
            - Space: O(1).
        """
        self._s1_to_s2()
        data = self._s2.pop()
        self._s2_to_s1()

        return data

    def _s1_to_s2(self) -> None:
        while not self._s1.is_empty():
            self._s2.push(self._s1.pop())

    def _s2_to_s1(self) -> None:
        while not self._s2.is_empty():
            self._s1.push(self._s2.pop())


@dataclass
class Animal:
    name: str
    arrival: datetime = None


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalQueueError(Exception):
    pass


class AnimalQueue:
    """A data structure for an Animal Shelter with cats and dogs.
    People can only adopt (dequeue) the "oldest" animal, cat or dog."""
    def __init__(self) -> None:
        self._cats = deque()
        self._dogs = deque()

        self._animals_by_type = {
            Cat: self._cats,
            Dog: self._dogs
        }

    def enqueue(self, animal: Animal) -> None:
        """Adds an animal to the queue.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        species = type(animal)

        if species not in self._animals_by_type:
            raise NotImplementedError(
                "Animal of type {} is not allowed. Choose from {}."
                .format(type(animal), list(self._animals_by_type.keys())))

        animal.arrival = datetime.now().isoformat()
        self._animals_by_type[species].append(animal)

    def dequeueAny(self) -> Animal:
        """Removes the oldest animal from the queue.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        animals = []

        if self.has_dogs():
            animals.append(self._dogs[0])

        if self.has_cats():
            animals.append(self._cats[0])

        if not animals:
            raise AnimalQueueError("Animal shelter has no animals.")

        oldest_animal = sorted(animals, key=lambda a: a.arrival)[0]

        return self._animals_by_type[type(oldest_animal)].popleft()

    def dequeue_dog(self) -> Dog:
        """Removes the oldest dog from the queue.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        return self._dogs.popleft()

    def dequeue_cat(self) -> Cat:
        """Removes the oldest cat from the queue.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        return self._cats.popleft()

    def has_dogs(self) -> bool:
        """Checks if the queue has dogs."""
        return len(self._dogs) > 0

    def has_cats(self) -> bool:
        """Checks if the queue has cats."""
        return len(self._cats) > 0
