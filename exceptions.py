# Syntax error when parser detects incorrect syntax for a statement
# Exceptions are when an error occurs while the script is running. 
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as zero_division_error:
    print(zero_division_error)
except TypeError as type_error:
    print(type_error)
    
    