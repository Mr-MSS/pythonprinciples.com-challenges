"""
Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""

def only_ints(num1,num2):
    # check if both of the given parameters are intgers
    if type(num1) is int and type(num2) is int:
        return True
    else:
        return False

print(only_ints(1,2))
print(only_ints("a",1))