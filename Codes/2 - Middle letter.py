"""
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

def mid(string):
    # get the string length
    num = len(string)
    # if the string length is even, then there is no middle letter
    if num % 2 == 0:
        return ""
    # if string length is odd number, then we can divide by 2 and remove fractions by using int()
    else:
        # go to the middle index that we calculated
        return string[int(num/2)] # another way is to use (//) e.g string[num//2]
        
print(mid("abc"))