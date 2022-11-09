# Python Sorting Algorithms

# Python has a built-in list of sorting algorithms that you can use to sort lists.

# The list of sorting algorithms are:

# 1. sort() - Sorts the list ascending by default.

# 2. reverse() - Reverses the sorting order of the list.

# 3. sorted() - Sorts the list in a function, and returns a new list, leaving the original list unchanged.

# 4. sort(reverse = True) - Sorts the list in descending order.

# 5. sort(key = myFunc) - Sorts the list, using a specified function to determine the sorting criteria.

# 6. sort(reverse = True, key = myFunc) - Sorts the list in descending order, using a specified function to determine the sorting criteria.

# 7. sorted(iterable, key = myFunc) - Sorts the specified iterable object, using a specified function to determine the sorting criteria.

# 8. sorted(iterable, reverse = True, key = myFunc) - Sorts the specified iterable object in descending order, using a specified function to determine the sorting criteria.

# Example 1: Sort a list of numbers

# Create a list of numbers

numbers = [3, 1, 6, 2, 8]

# Time complexity: O(n log n) - where n is the number of elements in the list to be sorted.

# Space complexity: O(n) - where n is the number of elements in the list to be sorted.

# Sort the list

numbers.sort()

# Print the sorted list

print(numbers)

# Output: [1, 2, 3, 6, 8]

# Example 2: Sort a list of strings

# Create a list of strings

strings = ["banana", "Orange", "Kiwi", "cherry"]

# Sort the list

strings.sort()

# Print the sorted list

print(strings)

# Output: ['Kiwi', 'Orange', 'banana', 'cherry']

# Time Complexity: O(n log n) - where n is the number of elements in the list to be sorted.

# Space Complexity: O(n) - where n is the number of elements in the list to be sorted.

# You can see in the example above that the sort() method sorts the list in ascending order by default. The sort() method is case sensitive, which means that capital letters come before lower case letters.

