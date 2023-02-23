# pop()
# removes and returns element having given key
square={'1**2':1,'2**2':4,'3**2':9,'4**2':16,'5**2':25,'6**2':36,'7**2':49}

print(square)

square.pop('1**2')
print(square)
# {'2**2': 4, '3**2': 9, '4**2': 16, '5**2': 25, '6**2': 36, '7**2': 49}

square.pop('4**2')
print(square)
# {'2**2': 4, '3**2': 9, '5**2': 25, '6**2': 36, '7**2': 49}
