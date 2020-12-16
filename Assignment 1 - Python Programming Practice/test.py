from a1_include import *

def right_Rotate(arr, new_array, num):
    """
    Function that takes the current array, new_array, and number of rotations. This
    function will only rotate to the right "num" amount of times. This will return
    a new array with the correct number of rotations from given arr.
    """
    length = arr.size()
    i = 0
    for item in range(length - num, length): #copies items from specified start point
        new_array.set(i, arr.get(item))
        i += 1

    for item in range(0, length - num): #copies items from the rest of the array
        new_array.set(i, arr.get(item))
        i += 1

    return new_array


def left_Rotate(arr, new_array, num):
    """
        Function that takes the current array, new_array, and number of rotations. This
        function will only rotate to the left "num" amount of times. This will return
        a new array with the correct number of rotations from given arr.
    """
    length = arr.size()
    i = 0
    for item in range(num, length): #will copy to new array from specified start point
        new_array.set(i, arr.get(item))
        i += 1

    for item in range(0, num):
        new_array.set(i, arr.get(item))
        i += 1

    return new_array

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This function takes a StaticArray and step parameter. This function will return
    a new StaticArray
    """
    length = arr.size()
    new_array = StaticArray(arr.size())

    #rotate left
    if steps < 0:
        steps = abs(steps)
        if steps > length:
            remainder = steps - length
            while remainder >= length: #will find the correct starting point when to copy new array
                remainder -= length
            new_array = left_Rotate(arr, new_array, remainder)
        else:
            new_array = left_Rotate(arr, new_array, steps)

        return new_array

    #rotate right
    if steps >= 0:
        if steps > length:
            remainder = steps - length
            while remainder >= length: #will find the correct starting point when to copy new array
                remainder -= length
            new_array = right_Rotate(arr, new_array, remainder)
        else:
            new_array = right_Rotate(arr, new_array, steps)

    return new_array


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
