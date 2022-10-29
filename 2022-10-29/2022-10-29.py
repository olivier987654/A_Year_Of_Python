## Python List Methods, this project shows different ways to list things in a list. 

def main():
    print("Hello, World!") # This is a comment 

    # Data Structures list 

    # List of integers

    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # List of strings

    str_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    # List of floats

    float_list = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]

    # List of lists

    list_list = [int_list, str_list, float_list]

    # List of tuples,  a tuple is an immutable list 

    tuple_list = [(1, "one", 1.1), (2, "two", 2.2), (3, "three", 3.3), (4, "four", 4.4), (5, "five", 5.5), (6, "six", 6.6), (7, "seven", 7.7), (8, "eight", 8.8), (9, "nine", 9.9), (10, "ten", 10.10)]

    # List of dictionaries, in this list each dictionary has a key and a value like a hash table. 

    dict_list = [{"int": 1, "str": "one", "float": 1.1}, {"int": 2, "str": "two", "float": 2.2}, {"int": 3, "str": "three", "float": 3.3}, {"int": 4, "str": "four", "float": 4.4}, {"int": 5, "str": "five", "float": 5.5}, {"int": 6, "str": "six", "float": 6.6}, {"int": 7, "str": "seven", "float": 7.7}, {"int": 8, "str": "eight", "float": 8.8}, {"int": 9, "str": "nine", "float": 9.9}, {"int": 10, "str": "ten", "float": 10.10}]


    # List of sets, a set is a list of unique values

    set_list = [{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}, {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10}]

    # List methods 

    # append() adds an item to the end of the list

    int_list.append(11) # adds 11 to the end of the list

    print(int_list)

    # clear() removes all items from the list

    clear(int_list) # removes all items from the list 

    print(int_list)

    # copy() returns a copy of the list

    copy_list = int_list.copy() # this line makes a copy of the desired list.

    print(copy_list)

    # count() returns the number of elements with the specified value

    count_list = int_list.count(1) # this line counts the number of times 1 appears in the list

    print(count_list)

    # extend() adds the elements of a list (or any iterable), to the end of the current list

    extend_list = int_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # this line adds the numbers 1-10 to the end of the list 

    print(extend_list)

    # index() returns the index of the first element with the specified value

    index_list = int_list.index(1) # this line returns the index of the first 1 in the list

    print(index_list)

    # insert() adds an element at the specified position 

    insert_list = int_list.insert(0, 1) # this line inserts a 1 at the beginning of the list

    print(insert_list)

    # pop() removes the element at the specified position

    pop_list = int_list.pop(0) # this line removes the first item in the list

    print(pop_list)

    # remove() removes the first item with the specified value

    remove_list = int_list.remove(1) # this line removes the first 1 in the list

    print(remove_list)

    # reverse() reverses the order of the list

    reverse_list = int_list.reverse() # this line reverses the order of the list

    print(reverse_list)

    # sort() sorts the list

    sort_list = int_list.sort() # this line sorts the list

    print(sort_list)
