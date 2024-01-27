"""
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""

def consecutive_zeros(binrayNum):
    # seperate the string by the 1s using split("1"), e.g 1001101000 will become (00 0 000)
    binrayNum = sorted(binrayNum.split("1"))
    # access the last item in the list (as the last item is the max after using sorted())
    binrayNum = len(list(binrayNum[len(binrayNum)-1]))
    return binrayNum

biNum = "1001101000110"

print(consecutive_zeros(biNum))