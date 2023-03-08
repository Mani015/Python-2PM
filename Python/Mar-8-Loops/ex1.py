
# BREAK:
# The break statement is used inside the loop to exit out of the loop.
# It is useful when we want to terminate the loop as soon as the condition is fulfilled instead of doing the remaining iterations.
# It reduces execution time.
# Whenever the controller encountered a break statement, it comes out of that loop immediately



for i in range(20):
    if i==15:
        break
    print(i,end=' ')
print()
print('loop exist')

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# loop exist

