"""
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(string):
    # container list
    indexList = []
    indexCounter = -1
    # take every single item (letter) and check if it is capital or not
    for i in string:
        if  i == i.upper():
            indexCounter += 1
            # add letter index to our container (append to our list)
            indexList.append(indexCounter)
        else:
            indexCounter += 1
    return indexList

print(capital_indexes("HeLlO"))