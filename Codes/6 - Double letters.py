"""
Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True
if there are two identical letters in a row in the string, and False otherwise.
"""

def double_letters(string):
    # check if the given string is empty
    if string == "":
        return False
    # using try/except to avoid going out of index when using string[i+1]
    try:
        # go through all the items of the given string
        for i in range(len(string)):
            # compare the current letter with the next letter in the string
            if string[i] == string[i+1]:
                return True
    except:
        return False

print(double_letters('hello'))