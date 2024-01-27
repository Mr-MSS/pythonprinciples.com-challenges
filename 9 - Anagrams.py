"""
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""

# method 1
def is_anagram(str1, str2):
    # convert string1 to a list
    str1 = list(str1)
    # convert string2 to a list
    str2 = list(str2)
    # sort each list
    str1.sort()
    str2.sort()
    # return True or False by comparing the 2 sorted lists
    return sorted(str1) == sorted(str2)

# method 2
def is_anagram(str1, str2):
    # return True or False by comparing the 2 sorted lists
    return sorted(str1) == sorted(str2)

print(is_anagram("typhoon", "opython"))
print(is_anagram("Alice", "Bob"))
