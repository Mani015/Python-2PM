# copy():The copy() method returns a shallow copy of a list.
# The copied list points to a different memory location than the original list,
# so changing one list does not affect another list.

y = [11,22,33,44,55,66,77,88,99]
print(y)

print(y.copy())
# [11, 22, 33, 44, 55, 66, 77, 88, 99]
# [11, 22, 33, 44, 55, 66, 77, 88, 99]

x2 = y.copy()
print(x2)
# [11, 22, 33, 44, 55, 66, 77, 88, 99]