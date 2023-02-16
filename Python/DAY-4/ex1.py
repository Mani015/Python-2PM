# list is a mutable datatype

x=[1,2,3]
# print(type(x))
# <class 'list'>

# append:Adds an element at the end of the list
x.append(4)
# print(x)
x.append(7)
# print(x)
# [1, 2, 3, 4, 7]


x.append('java','python')
# print(x)
# TypeError: list.append() takes exactly one argument (2 given)