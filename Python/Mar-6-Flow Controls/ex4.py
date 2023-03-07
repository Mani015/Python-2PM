print('WELCOME TO TEMPLE RUN ')
print()
print('lets start')
l1=int(input('Enter 1st level'))

if l1==1:
    print('level 1 complete succesfully')
    print('Wel come to next level')
    l2=int(input('Enter 2nd level:'))
    if l2==2:
        print('level2 complete successfully')
        print('welcome to 3rd level')
        l3=int(input('Enter 3rd level'))
        if 3==l3:
            print('level 3 complete successfully')


        else:
            print('you are failed 3rd level')
    else:
        print('you are fail 2nd level')

else:
    print('you are fail')

print('Thanks for playing')