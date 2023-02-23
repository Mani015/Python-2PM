# popitem()

square={'1**2':1,'2**2':4,'3**2':9,'4**2':16,'5**2':25,'6**2':36,'7**2':49}
print(square)
# {'1**2': 1, '2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25, '6**2': 36, '7**2': 49}
square.popitem()
print(square)
# {'1**2': 1, '2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25, '6**2': 36}

square.popitem()
print(square)
# {'1**2': 1, '2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25}


square.popitem('2**2')
print(square)
# TypeError: dict.popitem() takes no arguments (1 given)
