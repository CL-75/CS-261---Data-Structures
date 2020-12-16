# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 6
# Description: A function that receives a StaticArray and returns an int that describes whether the array is sorted.
#              Method should return 1 if sorted in strictly ascending order
#              Method should return 2 if sorted in strictly descending order
#              Method should return 0 if sorted another way


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    
    """
    Function will recevie a StaticArray as a param and check the order of the values within.
    Will return 1 if sorted in ascending order, 2 if descending, 0 if sorted by neither.
    """

    ascend = True
    
# Checking if values are in ascending order
    while ascend == True:
        for i in range(0, arr.size() - 1):
            if arr.get(i) < arr.get(i + 1):
                ascend = True

# Breaking loop if not in ascending order
            else:
                ascend = False
                break

        if ascend == True:
            return 1


# Checking if values are in descending order
    while ascend == False:
        for i in range(0, arr.size() - 1):
            if arr.get(i) > arr.get(i + 1):
                ascend = False

# Breaking loop if not in descending order
            else:
                ascend = None
                break

        if ascend == False:
            return 2


# If values are neither
        if ascend == None:
          return 0




# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
