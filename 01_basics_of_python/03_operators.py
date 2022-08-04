'''
    Operators are used to perform different operations on the variables or simple on data.
'''

'''
    Arithmetic operators are used to perform arithmetic operations on the data, like addition, subtraction, etc...
    order of precedence : 
        () parenthesis
        ** exponential
        % module * multiplication / float division // integer division
        + addition - subtraction
'''

ans = 3 + 5 // 2 * 5 / (9**2)
print(ans)

'''
    Comparision operators :
    -> comparing operators are used to compare the values mathematically. the answer will be either true or false.
    < > == != <= >=
    is -> equal to
    is not -> not equal to
'''
val1 = 5
val2 = 4
print(val1 is val2)

'''
    Logical operators are used for evaluating the boolean logical expressions
    AND
    OR
    NOT
'''

print(True and False)
print(True or False)
print(not True)

'''
    String operations :
    + concatenation
    * multiply a string (repeat the string for n times)
    'in' used to search in another search returns true or false;
'''

first_name = "python"
last_name = "programming"

ext = "py"

print(first_name + " " +  last_name)
print(first_name*3)
print(ext in first_name)