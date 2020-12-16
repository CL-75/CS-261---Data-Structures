# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 8
# Description: Function that receives a StaticArray where elements are already sorted in order and returns
#              a new StaticArray with duplicate values removed. 


from a1_include import *


def remove_duplicates(arr: StaticArray) -> StaticArray:
    
    """
    Function will receive StaticArray as a param with elements already sorted.
    Will return a new StaticArray with duplicate values removed.
    """

    nums = 0

    # this code applies if there's only one value in the StaticArray
    if arr.size() == 1:
        new_arr = StaticArray(1)
        new_arr.set(nums, arr.get(0))
        return new_arr

# Finding original values without duplicates
    for i in range(0, arr.size() - 1):
        if arr.get(i) != arr.get(i + 1):
            nums += 1
    nums += 1

    new_arr = StaticArray(nums)

# Comparing values
    x = 0
    for i in range(0, arr.size() - 1):
        if arr.get(i) != arr.get(i + 1):
            new_arr.set(x, arr.get(i))
            x += 1
    new_arr.set(x, arr.get(arr.size() - 1))

        
    return new_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
