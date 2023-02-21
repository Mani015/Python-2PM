# The differnece between remove () and Disscard():
# Python provides the discard() method and remove() method which can be used to remove the items from the set.
# The difference between these function, using discard() function
# if the item does not exist in the set then the set remain unchanged whereas remove() method will through an error

car = {'benz','toyoto','bmw','scorpio','mahi','ferrari','kia','buggati','innova','audi','jaguar','tata'}
print(car)

# print(car)
# {'scorpio', 'ferrari', 'bmw', 'tata', 'toyoto', 'mahi', 'jaguar', 'buggati', 'innova', 'audi', 'benz', 'kia'}
#
# car.remove('scorpio')
# print(car)
# {'bmw', 'benz', 'mahi', 'toyoto', 'innova', 'ferrari', 'tata', 'jaguar', 'kia', 'buggati', 'audi'}

# car.discard('xyz')
# print(car)
# print('discard')

# car.remove('123')
# print(car)

# print(car.discard('asdf'))



# pop(): Generally, the pop() method will always remove the last item but the set is unordered,
# we can't determine which element will be popped from set.
car.pop()
print(car)
car.pop()
print(car)
