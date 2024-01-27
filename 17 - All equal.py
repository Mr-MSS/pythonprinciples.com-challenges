"""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""

# short solution but is vulnerable to palindromes. e.g ["b", "o", "b"] returns True
def all_equal(eList):
    # reverse the list and compare it to the original list
    return eList[::-1] == eList

# Short version (pythonprinciples.com solution)
def all_equal(eList):
    return all(item1 == item2 for item1 in items for item2 in items)

print(all_equal([1,1,1]))
print(all_equal(["l","o","l"]))
