"""
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""

# this solution validates using indexes and slicing
def validate(str1):
    str2 = str1.split(":")
    if str1[:3] == ("def"):
        if (":") in str1:
            if ("(") and (")") in list(str2[0]):
                if (str1.split(":")[0].split()[1][-2]) != ("("):
                    if (str1.split("\n")[1][:4]) == ("    "):
                        if (str1.split()[1][:8]) == ("validate"):
                            if ("return") in (str1.split()):
                                return True
                            return "missing return"
                        return "wrong name"
                    return "missing indent"
                return "missing param"
            return "missing paren"
        return "missing :"
    return "missing def"

# Short version (pythonprinciples.com solution)
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True