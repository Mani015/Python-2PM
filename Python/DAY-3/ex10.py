# SORT():The list.sort() method sorts the elements of a list in ascending or descending order
# using the default < comparisons operator between items.
names = [2,4,3,1,2,3,4,5,67,8,9,10,-2,1,-1,-12]

# names.sort()
# print(names)
# [-12, -2, -1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 9, 10, 67]

names.sort(reverse=True)
# print(names)
# [67, 10, 9, 8, 5, 4, 4, 3, 3, 2, 2, 1, 1, -1, -2, -12]


x = ['d','g','y','r','u','k','c','s','m','p','o']
x.sort()
print(x)
# ['c', 'd', 'g', 'k', 'm', 'o', 'p', 'r', 's', 'u', 'y']
x.sort(reverse=True)
print(x)
# ['y', 'u', 's', 'r', 'p', 'o', 'm', 'k', 'g', 'd', 'c']
