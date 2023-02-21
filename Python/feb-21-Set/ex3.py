
s1 = {1,2,3,4,5,6,'a','b','c','d','r'}

# print(s1)
# {1, 2, 3, 4, 5, 6, 'a', 'd', 'c', 'b', 'r'}
# Sets are mutable which means we can modify it after its creation.

# whereas the update() method is used to add multiple elements to the set.
s1.update({11,22,33,44})
print(s1)
# {1, 2, 3, 4, 5, 6, 33, 'r', 11, 'b', 44, 'a', 22, 'd', 'c'}


s1.update({'apple','banana','orange','melon'})
print(s1)
# {1, 2, 3, 4, 5, 6, 'b', 'd', 11, 'r', 'melon', 22, 'c', 'banana', 33, 'a', 'apple', 44, 'orange'}
