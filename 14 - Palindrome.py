"""
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
"""

# Solution 1
def palindrome(string):
    # check if the string = itself but in backwards order
    if string == string[::-1]:
        return True
    else:
        return False
    
# Short version (pythonprinciples.com solution)
def palindrome(string):
    return string == string[::-1]

print(palindrome("bob"))