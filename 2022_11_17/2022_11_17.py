## Python 2D list

# A 2D list is a list of lists. It is a list of lists where each list is a row in the 2D list.

my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a 2D list

# To access an element in a 2D list, you need to specify the row and column of the element.

# For example, to access the element 5, you need to specify the row 1 and column 1.

# Example:

# Code Example:

my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(my_list_of_lists[1][1])

# Output: 5

# Add a list to 2D list

# To add a list to a 2D list, you can use the append() method.

# Example:

# Code Example:

my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_list_of_lists.append([10, 11, 12])

print(my_list_of_lists)

# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Remove a list from 2D list

# To remove a list from a 2D list, you can use the pop() method.

# Example:

# Code Example:

my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_list_of_lists.pop(1)

print(my_list_of_lists)

# Output: [[1, 2, 3], [7, 8, 9]]