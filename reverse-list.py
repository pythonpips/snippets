"""author: @pythonpips"""

numbers = [1, 2, 3, 4, 5]

# Slice the list
numbers[::-1]
>>> [5, 4, 3, 2, 1]

# reversed generator
list(reversed(numbers))
>>> [5, 4, 3, 2, 1]

# reverse method to reverse the list in-place
numbers.reverse()
print(numbers)
>>> [5, 4, 3, 2, 1]
