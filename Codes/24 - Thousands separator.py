"""
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""

def format_number1(Number):
    # Check if the given number is negative
    if Number < 0:
        return "Negative!"
    
    else:
        # Convert the given number to a list
        ListNumber = list(str(Number))
        
        # Find out how many commas we need for our number
        if len(ListNumber) % 3 == 0: # Commas number is [(total digits / 3) - 1] --> (if remainder = Zero)
            num0 = int(len(ListNumber) / 3) - 1
        else: # Commas number is [total digits / 3] --> (if remainder is NOT Zero)
            num0 = int(len(ListNumber) / 3)
        
        # Reverse our list
        ListNumber.reverse()
        
        # Steps counter
        j = 3
        
        # Put a comma in after every 3 digits
        for i in range(num0):
            ListNumber.insert(j+i, ',')
            j = j + 3
        
        # Reverse list to original order
        ListNumber.reverse()
        
        # string container
        word = str()
        
        # Add all index items to one string
        for i in ListNumber:
            word = word + i
            
        return word


# Shorter solution
def format_number2(num):
    if num >= 0:
        num1 = list(str(num))
        commasNum = int(len(num1) / 3)
        j = -3
        for i in range(commasNum):
            num1.insert(j-i, ',')
            j = j - 3
        word = ''.join(num1)
        return word.lstrip(",")
    else:
        return "Negative!"


# Short version (pythonprinciples.com solution)
# built-in solution
def format_number3(n):
    return "{:,}".format(n)

print(format_number1(1000000))
print(format_number2(1000000))
print(format_number3(1000000))