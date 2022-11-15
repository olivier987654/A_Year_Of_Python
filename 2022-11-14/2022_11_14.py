## Python data structure : Queue

# Queue is a linear structure which follows a particular order in which the operations are performed.

# The order is First In First Out (FIFO).

# A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

# Example:

# Code Example:

queue = ["1", "2", "3"]

queue.append("4")

queue.append("5")

print(queue)

queue.pop(0)

print(queue)

