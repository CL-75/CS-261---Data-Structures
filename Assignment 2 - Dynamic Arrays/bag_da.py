# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 2 - bag_da.py
# Description: Writing add, remove, count, and clear methods for Bag class.
# Last revised: 10/19/2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()




    def add(self, value: object) -> None:
        """
        This method will add a value 
        """

        self.da.append(value)
        


    def remove(self, value: object) -> bool:
        """
        This method will remove the given value. 
        False will be returned if the value is not found, True if found
        """

        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True                   # Returning True if value is found
        return False                  # Returning False if value not found

        

    def count(self, value: object) -> int:
        """
        This method will count how many times the given value appears in 
        the array.
        """
        val_count = 0

        for i in range(self.size()):
            if value == self.da.get_at_index(i):  # Checking if given value is in the array and incrememnting the variable by 1
                val_count += 1

        return val_count
     
        

    def clear(self) -> None:
        """
        This method clears all the contents of the bag
        """

        for i in range(self.size()):
            self.da.remove_at_index(0)
        


    def equal(self, second_bag: object) -> bool:
        """
        Compares the content of the current bag with that of the second bag provided by the user.
        Returns True if bags are equal, False if not. Both Bags must have the same number
           of elements and the same elements to be equal. Order does not matter in the Bags.
        """

        if self.size() != second_bag.size():
            return False

        for i in range(self.size()):
            found = False
            for x in range(self.size()):
                if self.da.get_at_index(i) == second_bag.da.get_at_index(x):
                    found = True
            if found is False:
                return False

        return True




# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
