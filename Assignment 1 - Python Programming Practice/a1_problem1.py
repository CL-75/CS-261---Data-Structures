# Course: CS261 - Data Structures
# Student Name: Casey Levy 
# Assignment: Assignment 1 - Problem 1
# Description: Write a function that receives a one dimensional array of integers and returns a Python tuple with two values - minimum and maximum values in the input array.


from a1_include import *


def min_max(arr: StaticArray) -> ():
    """
    This function receives a list ands returns the min and max values
    """

# Setting the first value of the array as both the min and max values
    min, max = arr.get(0), arr.get(0)

# Finding the minimum value
    for val in range(arr.size()):
        if arr.get(val) < min:
            min = arr.get(val)

# Finding the maximum value
        elif arr.get(val) > max:
            max = arr.get(val)

    return min, max



# BASIC TESTING
if __name__ == "__main__":

    # example 1
    arr = StaticArray(5)
    for i, value in enumerate([8, 7, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    # example 2
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    # example 3
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))
