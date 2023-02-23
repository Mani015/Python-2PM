
dc1 = {1:'apple',2:'mango',3:'orange',4:'banana',5:'graphes',6:'kiwi'}
print(dc1)
# {1: 'apple', 2: 'mango', 3: 'orange', 4: 'banana', 5: 'graphes', 6: 'kiwi'}
#
# Without value:
dc1.setdefault(7)
print(dc1)
# {1: 'apple', 2: 'mango', 3: 'orange', 4: 'banana', 5: 'graphes', 6: 'kiwi', 7: None}

# With value
dc1.setdefault(8,'melon')
print(dc1)
# {1: 'apple', 2: 'mango', 3: 'orange', 4: 'banana', 5: 'graphes', 6: 'kiwi', 7: None, 8: 'melon'}


# empty setdefault()
dc1.setdefault()
print(dc1)
# TypeError: setdefault expected at least 1 argument, got 0