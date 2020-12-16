# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 3
# Description: Reversing the order of values within a given StaticArray


from a1_include import *


def reverse(arr: StaticArray) -> None:

    """
    Taking a StaticArray and reversing the order of the values, 'in-place'.
    No new array will be created.
    """

    arr_length = arr.size()

    for i in range(int(arr_length / 2)):
        place = arr.get(i)
        arr.set(i, arr.get(arr_length - i - 1))   # Setting the first value to the last value
        arr.set(arr_length - i - 1, place)        # Setting last value to the first value
        
    return 


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
