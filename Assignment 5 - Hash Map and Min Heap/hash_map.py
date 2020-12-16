# Course: CS261 - Data Structures
# Assignment: 5 - hash_map.py
# Student:
# Description: Creating various methods for hash map


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out



    def clear(self) -> None:
        """
        Clears the hash map and all contents
        """
        for i in range(self.capacity):       # Clearing bucket
            self.buckets.pop()

        for i in range(self.capacity):
            self.buckets.append(LinkedList())    # Making new empty bucket, setting with same capacity

        self.size = 0




    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key. None is returned
           if the key is not in the hash map.
        """
        hash_map = self.hash_function(key)
        ind = hash_map % self.capacity
        temp = self.buckets.get_at_index(ind)

        if temp.contains(key) is None:         # Case if given key isn't there
            return None

        else:
            return temp.contains(key).value



    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If a given key already exists
           its associated value should be replaced with the new value. If a given key is not there,
           the pair shall be added.
        """
        hash_map = self.hash_function(key)      # Finding proper index in DynArray
        ind = hash_map % self.capacity

        lst = self.buckets.get_at_index(ind)

        if lst.contains(key) is None:              # If key is not there
            lst.insert(key, value)
            self.size += 1

        else:
            lst.contains(key).value = value       # Updating value if key is found



    def remove(self, key: str) -> None:
        """
        Method removes the key and its associated value from the hash map.
        If a given key is not in the hash map, the method does nothing.
        """
        hash_map = self.hash_function(key)         # Finding proper index in DynArray
        ind = hash_map % self.capacity

        if self.buckets.get_at_index(ind).remove(key):     # Utilizing remove function to remove SLNode
            self.size -= 1



    def contains_key(self, key: str) -> bool:
        """
        Returns True if given key is in the hash map. Otherwise, returns False.
        """
        hash_map = self.hash_function(key)      # Finding proper index in DynArray
        ind = hash_map % self.capacity

        if self.buckets.length() == 0:          # Case if HashMap is empty
            return False

        cur = self.buckets.get_at_index(ind)
        if cur.contains(key) is None:
            return False

        if cur.contains(key) is not None:
            return True



    def empty_buckets(self) -> int:
        """
        Returns a number of empty buckets in the hash table
        """
        num = 0

        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:
                num += 1
        return num




    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        return float(self.size / self.capacity)




    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table. All existing data must
           remain in the new hash map and all links must be rehashed. Method does nothing
           if new_capacity is less than 1.
        """
        if new_capacity < 1:
            return

        new_arr = DynamicArray()                 # Creating new hash DynArray with new capacity
        for i in range(new_capacity):
            new_arr.append(LinkedList())

        for i in range(self.capacity):            # Traverse through original DynArray
            cur = self.buckets.get_at_index(i)

            for j in cur:
                hash_value = self.hash_function(j.key)
                new_index = hash_value % new_capacity
                new_arr.get_at_index(new_index).insert(j.key, j.value)

        self.buckets = new_arr                   # Updating data
        self.capacity = new_capacity



    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stored in the hash map.
        Order of the keys does not matter.
        """
        arr = DynamicArray()
        for i in range(self.capacity):             # Appending keys to new DynArray
            cur = self.buckets.get_at_index(i)
            for j in cur:
                arr.append(j.key)

        return arr



# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
