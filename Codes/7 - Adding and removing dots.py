"""
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""

def add_dots(string):
    # container
    str1 = []
    # convert the string to a list and append "." between all the list items (letters)
    for i in list(string):
        str1.append(i)
        str1.append(".")
    # remove the "." dot at the end of the list using pop()
    str1.pop()
    # convert the list to a single string
    str1 = ''.join(str1)
    return str1
    
def remove_dots(string):
    # remove the dots from the given string using split()
    string = string.split(".")
    # convert the list to a single string
    string = ''.join(string)
    return string


string = "test"
print(remove_dots(add_dots(string)))