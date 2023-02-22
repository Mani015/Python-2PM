x1={'a','b','c','d',1,2,3,4,5,6,7,8,11}
x2={11,22,33,44,55,66,'a','b'}

# print(f'before updating:',x1)
# # before updating: {1, 2, 3, 'c', 4, 5, 6, 7, 8, 'b', 11, 'a', 'd'}
# print(x1.intersection_update(x2))
# print('After updating:',x1)
# # After updating: {'b', 11, 'a'}


# print(x1.difference(x2))
# {1, 2, 3, 4, 5, 6, 7, 8, 'c', 'd'}

# print(x2.difference(x1))
# {33, 66, 44, 22, 55}
#
# print(x1.difference_update(x2))
# print(x1)
#
# print('____________________________________________________________')
# Updates Calling Set With Intersection of Sets
# print(x2.difference_update(x1))
# print(x2)

# print(x1.intersection(x2))

# print(x2.intersection(x1))

# x1.intersection_update(x2)
# print(x1)
# Updates Calling Set With Intersection of Sets
x2.intersection_update(x1)
print(x2)