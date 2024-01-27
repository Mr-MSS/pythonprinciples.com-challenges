"""
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""

def largest_difference(numList):
    # by using sorted(), we get a sorted list starting from the smallest and onwards
    # (numList)[-1] = last item in the list) - (numList)[-1] = first item in the list)
    return sorted(numList)[-1] - sorted(numList)[0]

print(largest_difference([1, 2, 3]))