"""
Counting parameters
Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
"""

def param_count(*args):
    # Container
    j = []
    # go through all the given args
    for i in args:
        # append every single arg to a list
        j.append(i)
    # return the list length which is the number of args given to the fucntion
    return len(j)

# Short version (pythonprinciples.com solution)
def param_count(*args):
    return len(args)