# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 2 - queue_da.py
# Description: Writing enqueue and dequeue methods for Queue class.
# Last revised: 10/20/2020

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()



    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue
        """
        if self.size() == 0:
            self.da.append(value)     # Checking if empty and adding value if so

        else:    
            self.da.insert_at_index(self.size(), value)    # Adding value at proper location since queue isn't empty



    def dequeue(self) -> object:
        """
        Removes and returns the value from beginning of queue. If queue is empty, QueueException is raised.
        """
        if self.size() == 0:       # if empty queue
            raise QueueException

        val = self.da.get_at_index(0)    # Initializing val with first index position value

        self.da.remove_at_index(0)       # Removing element

        return val




# BASIC TESTING
if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
