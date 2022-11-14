## Quadratic time complexity in Python

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    for j in list:
        x = i * j
        print(x)

# Time Complexity of this algorithm is O(n^2) - where n is the number of elements in the list to be sorted.