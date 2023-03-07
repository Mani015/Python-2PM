# Nested if-else statement
# In Python, the nested if-else statement is an if statement inside another if-else statement.
# It is allowed in Python to put any number of if statements in another if statement.

# Syntax:
# if conditon_outer:
#     if condition_inner:
#         statement of inner if
#     else:
#         statement of inner else:
#     statement ot outer if
# else:
#     Outer else
# statement outside if block


num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if num1 >= num2:
    print(num1, 'is greater than ',num2)
else:
    print(num1, 'is smaller than', num2)
