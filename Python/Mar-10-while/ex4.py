
count = 0
number = 4

while count<number:
    password  = int(input('Enter your password:'))
    if password == 1:
        print('screen is open')
        break
    count = count+1
else:
    print('sorry ! there is no chances')
