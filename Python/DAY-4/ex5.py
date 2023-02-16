
cooldrinks = ['sprite','coke','maaza','limca','string','redbull','thumpsup','pepsi']

print(cooldrinks)
# ['sprite', 'coke', 'maaza', 'limca', 'string', 'redbull', 'thumpsup', 'pepsi']

# clear():Removes all the elements from the list
# cooldrinks.clear()
# print(cooldrinks)
# []



# remove():Removes the item with the specified value
cooldrinks.remove('redbull')
print(cooldrinks)

cooldrinks.remove('coke')
print(cooldrinks)
# ['sprite', 'maaza', 'limca', 'string', 'thumpsup', 'pepsi']

# cooldrinks.remove('string','pepsi')
# print(cooldrinks)
# TypeError: list.remove() takes exactly one argument (2 given)

cooldrinks.remove('fanta')
print(cooldrinks)
#ValueError: list.remove(x): x not in list

