# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 4
# Description: Function that recevies two parameters, a StaticArray and int value called "steps".
#              Will create and return a new StaticArray with all elements from original, but their
#              positions will be shifted left or right "steps" number of times, depending on if they're positive or negative.


from a1_include import *


def move_right(arr, new_arr, num):

    """
    Function takes parameters of a current array, new array, and "num" of steps.
    Number of steps determines how many places a value in the array moves right.
    Will return a new array with the new value rotations in place.
    """ 

    i = 0
    arr_length = arr.size()

# Copying items from specific points and then copying from the rest of the array
    for x in range(arr_length - num, arr_length):
        new_arr.set(i, arr.get(x))
        i += 1

    for x in range(0, arr_length - num):
        new_arr.set(i, arr.get(x))
        i += 1

    return new_arr



def move_left(arr, new_arr, num):

    """
    Function takes parameters of a current array, new array, and "num" of steps.
    Number of steps determines how many places a value in the array moves left.
    Will return a new array with the new value rotations in place.
    """ 

    i = 0
    arr_length = arr.size()

# Copying items from specific point
    for x in range(num, arr_length):
        new_arr.set(i, arr.get(x))
        i += 1

    for x in range(0, num):
        new_arr.set(i, arr.get(x))
        i += 1

    return new_arr



def rotate(arr: StaticArray, steps: int) -> StaticArray:

    """
    Creating a function that receives two parameters, a StaticArray, and an int value called "steps".
    The function will create and return a new StaticArray with same elements from original array but
    shifted left or right depending on the value of "steps". If "steps" is positive, elements will move right. 
    If not, elements move left. 
    """

    new_arr = StaticArray(arr.size())
    arr_length = arr.size()


#moving left
    if steps < 0:
        steps = abs(steps)
        
        if steps > arr_length:
            remain = steps - arr_length
            while remain >= arr_length:
                remain -= arr_length
            new_arr = move_left(arr, new_arr, remain)
        else:
            new_arr = move_left(arr, new_arr, steps)

        return new_arr
    

#moving right
    if steps >= 0:        
        if steps > arr_length:
            remain = steps - arr_length
            
            while remain >= arr_length:
                remain -= arr_length
            new_arr = move_right(arr, new_arr, remain)
        else:
            new_arr = move_right(arr, new_arr, steps)

    return new_arr




# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
        
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)
