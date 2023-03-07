# Ex: if, else

#
# num = int(input('Enter one number:'))
#
# if num%2==0:
#     print(f'{num} is a even number')
# else:
#     print(f'{num} is a odd number')



name = 'Python'
password = 1234
username = input('Enter your name:')
code = int(input('Enter your password:'))

if name==username and password==code:
    print('login successfully')
else:
    print('login fail')
# Enter your name:java
# Enter your password:1234
# login fail