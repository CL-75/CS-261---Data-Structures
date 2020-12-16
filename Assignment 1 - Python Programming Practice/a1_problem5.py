# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - Problem 5
# Description: A function that receives two integers, start and end, returns a StaticArray that contains consecutive
#              values that begin at start and end at "end"


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:

    """
    Function will take a "start" and "end" parameter. Returns a StaticArray that has values
    that are between "start" and "end"
    """

    new_arr = StaticArray(abs(start-end) + 1)
    x = 0

# if array is decreasing
    if start > end:
        new_arr.set(x, start)
        while start != end:
            x += 1
            start -= 1
            new_arr.set(x, start)

# if array is increasing
    else:
        new_arr.set(x, start)
        while start < end:
            start += 1
            x += 1
            new_arr.set(x, start)

    return new_arr




        

# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
