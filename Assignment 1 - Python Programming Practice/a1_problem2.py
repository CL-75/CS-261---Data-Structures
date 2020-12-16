# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 2
# Description: Function that takes a StaticArray as a parameter and creates a new array that is the same.
#              Will traverse the array and any value divisible by 3 will be changed to "fizz"
#              Any value divisible by 5 will be changed to "buzz"
#              Any value divisible by both will be changed to "fizzbuzz"


from a1_include import *


def fizz_buzz(arr: StaticArray) -> StaticArray:
    
    """
    Creating a function that takes a StaticArray as a parameter. A new array
    is created that is the same as the StaticArray being passed in. Each value
    that is divisible by 3 is changed to "fizz", each value divisible by 5 is
    changed to "buzz" and each value divisible by both is changed to "fizzbuzz".
    If none of the conditions apply, the value stays unchanged. The new array is
    then returned.
    """

    # Creating new array
    new_array = StaticArray(arr.size())

# Traversing the array and completing the given calculations for each element
    for i in range(arr.size()):
        if arr.get(i) % 3 == 0 and arr.get(i) % 5  == 0:   # If divisible by both 3 and 5
            new_array[i] = "fizzbuzz"
        
        elif arr.get(i) % 3 == 0:   # If only divisible by 3
            new_array[i] = "fizz"

        elif arr.get(i) % 5 == 0:   # If only divisible by 5
            new_array[i] = "buzz"

        else:
            new_array[i] = arr.get(i)

    return new_array

    


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
