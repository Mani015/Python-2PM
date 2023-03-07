

name = 'Python'
password = 1234
username = input('Enter your name:')
code = int(input('Enter your password:'))

if not(name==username and password==code):
    print('login successfully')
else:
    print('login fail')

# Enter your name:Python
# Enter your password:1234
# login fail

# ex: Mobile screen lock password
