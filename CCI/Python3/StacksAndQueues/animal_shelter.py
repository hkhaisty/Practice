import unittest


class LinkedList:
    class LinkedListNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, value):
        node = LinkedList.LinkedListNode(value)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        else:
            self.head = node

    def pop(self):
        if self.head is None:
            raise Exception('Nothing to pop.')

        data = self.head.data
        self.head = self.head.next

        return data

    def peek(self):
        if self.head is None:
            raise Exception('Nothing to peek.')

        return self.head.data

    def is_empty(self):
        return self.head is None


class Animal:
    def __init__(self, name):
        self._name = name
        self._age = None

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def is_older_than(self, animal):
        return self.age < animal.age


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.age = 0

    def enqueue(self, animal):
        animal.age = self.age
        self.age += 1
        if type(animal) is Cat:
            self.cats.push(animal)
        elif type(animal) is Dog:
            self.dogs.push(animal)

    def dequeue_any(self):
        if self.cats.is_empty():
            return self.dequeue_dogs()
        elif self.dogs.is_empty():
            return self.dequeue_cats()
        else:
            return self.dequeue_dogs() if self.dogs.peek().is_older_than(self.cats.peek()) else self.dequeue_cats()

    def dequeue_cats(self):
        return self.cats.pop()

    def dequeue_dogs(self):
        return self.dogs.pop()


class Test(unittest.TestCase):
    cat_values = ['Patches', 'Willy']
    dog_values = ['Ulf', 'Owain']

    def test_animal_shelter(self):
        animal_shelter = AnimalShelter()
        for cat, dog in zip(self.cat_values, self.dog_values):
            animal_shelter.enqueue(Cat(cat))
            animal_shelter.enqueue(Dog(dog))

        self.assertEqual('Ulf', animal_shelter.dequeue_dogs().name)
        self.assertEqual('Patches', animal_shelter.dequeue_cats().name)
        self.assertEqual('Willy', animal_shelter.dequeue_any().name)
        self.assertEqual('Owain', animal_shelter.dequeue_any().name)


if __name__ == '__main__':
    unittest.main()








