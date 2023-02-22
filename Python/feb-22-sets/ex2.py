x1={'a','b','c','d',1,2,3,4,5,6,7,8,11}
x2={11,22,33,44,55,66,'a','b'}
# Intersection:Returns Intersection of Two or More Sets

# print(x1.intersection(x2))
# {'a', 'b', 11}
# print(x2.intersection(x1))
# {'a', 'b', 11}



# Difference
# Syntax:set1.difference(set2)

# print(x1.difference(x2))
# {1, 2, 3, 'd', 'c', 4, 5, 6, 7, 8}

# print(x2.difference(x1))
# {33, 66, 44, 22, 55}

# print(x1)
# {1, 2, 3, 4, 5, 6, 7, 8, 11, 'd', 'b', 'a', 'c'}
# Difference update:
# print(x1.difference_update(x2))
# print(x1)
# {1, 2, 3, 4, 5, 6, 7, 8, 'd', 'c'}



print('before updating set:',x2)
# before updating set: {33, 66, 'a', 11, 44, 22, 55, 'b'}
print(x2.difference_update(x1))
print('after updating set',x2)
# after updating set {33, 66, 44, 22, 55}
