# Reverse():Reverses the order of the list
datatypes = ['integer',1,'string','collection of characters',12+6j,True,12.30]
# print(datatypes)
x= datatypes
# print(x)

# ['integer', 1, 'string', 'collection of characters', (12+6j), True, 12.3]
# ['integer', 1, 'string', 'collection of characters', (12+6j), True, 12.3]

x.reverse()
# print('using After reverse method:',x)
# using After reverse method: [12.3, True, (12+6j), 'collection of characters', 'string', 1, 'integer']


# count():Returns the number of elements with the specified value
y = [0,1,2,3,False,4,5,6,7,'real','img','list is orderd list',12.36,5.2,6.3,True]
# print(y.count(12.36))
# 1
# print(y.count(2))
# 1
print(y.count(1))
# 2


print(y.count(False))
# 2
























# k = 12+6j
# print(k)
#
# print(k.real)
# print(k.imag)