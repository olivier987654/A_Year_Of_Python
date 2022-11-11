# Python data structure : Stack

# Stack is a linear data structure which follows a particular order in which the operations are performed.

# The order may be LIFO(Last In First Out) or FILO(First In Last Out).

# Pushing(Adding) or popping(Removing) data from the stack.

# Code Example:

stack = ["1", "2", "3"]

stack.append("4")

stack.append("5")

print(stack)

stack.pop()

print(stack)

# For loop, a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in stack:
    if i == "4":
        stack.remove(i)

print(stack)

# Console Output:

# ['1', '2', '3', '4', '5']
# ['1', '2', '3', '4']
# ['1', '2', '3']



