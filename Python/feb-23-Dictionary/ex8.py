# Copy()
# eturns the Shallow Copy of a Dictionary
square={'1**2':1,'2**2':4,'3**2':9,'4**2':16,'5**2':25,'6**2':36,'7**2':49}

print(square.copy())
# {'1**2': 1, '2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25, '6**2': 36, '7**2': 49}
# Syntax: previous dictionary name . copy()------>
num = square.copy()
print(num)
# {'1**2': 1, '2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25, '6**2': 36, '7**2': 49}

print(type(num))
# <class 'dict'>