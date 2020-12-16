# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 7
# Description: Writing a function that receives a StaticArray and sorts the content in non-descending order.
#              Sorting must be done "in-place".


from a1_include import *


def sa_sort(arr: StaticArray) -> None:
    
    """
    Function receives StaticArray as a param, uses bubble sort
    to sort values. This wil change original value without creating a new StaticArray.
    """

    new_arr = arr.size() 

  # Traversing through array elements
    for i in range(new_arr):      
        for x in range(0, new_arr - i - 1): 

     # Traversing array and swapping if element is greater than the next
            if arr[x] > arr[x + 1] : 
                arr[x], arr[x + 1] = arr[x + 1], arr[x] 
    return


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
