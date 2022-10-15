# Using a hashmap to store the number of occurrences of each number in the array
# Time Complexity: O(n)
# Space Complexity: O(n)
# Hashmap definition : A hashmap is a data structure that stores key-value pairs. It is used to store data in an associative manner. It is a collection of key-value pairs where each key is mapped to a value. It is used to implement an associative array, a structure that can map keys to values. A hashmap uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

def findDuplicates(nums):
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    return [key for key, value in hashmap.items() if value == 2]







 
