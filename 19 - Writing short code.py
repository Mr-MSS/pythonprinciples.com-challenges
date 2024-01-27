"""
Writing short code
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.
"""

def convert(nums):
    # using list comprehensions to select every single item in the list and convert it to string
    return [str(i) for i in nums]

print(convert([1,2,3,4,5]))