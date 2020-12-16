# Course: CS261 - Data Structures
# Student Name: Casey Levy
# Assignment: Assignment 1 - dynamic_array.py
# Description: Writing multiple methods for Dynamic Array class
# Last revised: 10/18/2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        This method will change self.capacity with the new_capacity parameter.
        If new_capacity is less than 0 or less than the current size of the array, then we return nothing.
        A new StaticArray is then created that is twice the size of the current and all elements will be copied into it.
        """

        if new_capacity < 0 or new_capacity < self.size:
            return

        else:
            new_array = StaticArray(new_capacity)   # Creating a new array with the new capacity
            if new_capacity < self.data.size():
                for i in range(new_array.size()):   # Copying all elements into new array
                    new_array.set(i, self.data.get(i))

            else:
                for i in range(self.data.size()):
                    new_array.set(i, self.data.get(i))

        self.data = new_array
        self.capacity = new_capacity   # Setting references to the new array



    def append(self, value: object) -> None:
        """
        Takes a parameter and adds the value at the end of the current array.
        The resize() method will be called if the size == capacity.
        """

        if self.size == self.capacity:
            self.resize(self.capacity * 2)  # Resizing the capacity

        self.data.set(self.size, value)    # Size must be incremented each time append is called
        self.size += 1



    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adding a value at a specified index. If the array size == capacity, resize() will be called.
        All elements will be shifted right after insertion at specified index.
        """

        if self.size == self.capacity:      # Resizing the capacity
            self.resize(self.capacity * 2)

        if index < 0 or index > self.size:
            raise DynamicArrayException    # If index position is invalid

        for i in range(self.size-1, index-1, -1):  # Shifting elements to the right
            self.data.set(i+1, self.data.get(i))

        self.data.set(index, value)
        self.size += 1               # Value being inserted at specific index, size increased by 1



    def get_at_index(self, index: int) -> object:
        """
        Will return the value at the given index position
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException

        return self.data.get(index)



    def remove_at_index(self, index: int) -> None:
        """
        Removes value at specified index position. Before removing, will check if current size is less than 1/4th capacity.
        If so, the capacity will be modified to be double the current size but will stay above 10. Then shifts all elements to the left. 
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException

        if(self.size / self.capacity) < 0.25 and self.size >= 5:        # Checking if size is less than 1/4th capacity
            self.resize(self.size * 2)

        elif (self.size / self.capacity) < 0.25 and self.size < 5 and self.size > 1:   # Checking if capacity is at least 10
            self.resize(10)


        for x in range(index, self.size-1):         # Moving all elements to the left after above conditions are met/checked
            self.data.set(x, self.data.get(x+1))


        self.size -= 1    # Decreasing the size




    def slice(self, start_index: int, quantity: int) -> object:
        """
        Returning all values between given locations. Raises DynamicArrayException if either parameters are invalid.
        Will then return a new DynamicArray object.
        """
        new_array = DynamicArray()   # Creating new DynamicArray object to return at the end

        if start_index < 0 or start_index >= self.size or quantity < 0 or start_index+quantity > self.size:   # Testing conditional to ensure locations are valid
            raise DynamicArrayException

        try:
            for i in range(start_index, start_index+quantity):   
                new_array.append(self.data.get(i))                  # Copying values

        except DynamicArrayException:
            raise DynamicArrayException

        return new_array



    def merge(self, second_da: object) -> None:
        """
        Takes another DynamicArray object as a parameter and merges all elements/values into the current array in the same order as they
           are stored in the 2nd array.
        """
        for x in range(second_da.length()):
            self.append(second_da.get_at_index(x))




    def map(self, map_func) -> object:
        """
        Creates a new DynamicArray object where the value of each element is derived by applying the given map_func to the 
           corresponding value from the original array.
        """
        new_array = DynamicArray()

        for x in range(self.size):
            new_array.append(map_func(self.get_at_index(x)))

        return new_array




    def filter(self, filter_func) -> object:
        """
        Creates a new DynamicArray object populated with only the elements from the original array which filter_func returns True.
        """
        new_array = DynamicArray()

        for x in range(self.size):
            if filter_func(self.get_at_index(x)) == True:
                new_array.append(self.get_at_index(x))

        return new_array




    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Applies the given reduce_func to all elements of DynamicArray and returns resulting value. Takes an optional initializer parameter.
        If parameter is not given, the array's first value is used. If array is empty, method returns the value of initializer, or None.
        """

        if self.size == 0:
            return initializer

        if initializer is None:
            result = self.get_at_index(0)
            for i in range(1, self.size):
                result = reduce_func(result, self.get_at_index(i))

            return result

        elif initializer is not None:
            result = initializer
            for i in range(0, self.size):
                result = reduce_func(result, self.get_at_index(i))

        return result



# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    # remove_at_index - example 2
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
