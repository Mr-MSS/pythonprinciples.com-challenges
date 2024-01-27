"""
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""

def triple_and(bool1,bool2,bool3):
    # check if all the given parameters are True
    if bool1 and bool2 and bool3 == True:
        return True
    else:
        return False

# Short version (pythonprinciples.com solution)
def triple_and(bool1,bool2,bool3):
    return bool1 and bool2 and bool3