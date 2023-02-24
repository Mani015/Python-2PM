

# n1 = eval(input('Enter your 1st input:'))
#
# print(type(n1))
# print(n1)
# n2=eval(input('Enter your 2nd input:'))
#
# print(n1+n2)
# # 22
# print(n2+n1*2)
# # 34
# print(n1*n2/2)


Student_name = input('Enter your name:')
s1 = eval(input('Enter sub1 marks:'))
s2 = eval(input('Enter sub2 marks:'))
s3 = eval(input('Enter sub3 marks:'))
s4 = eval(input('Enter sub4 marks:'))
s5 = eval(input('Enter sub5 marks:'))
s6 = eval(input('Enter sub6 marks:'))

Student_Total_marks = s1+s2+s3+s4+s5+s6

print(f'{Student_name} total marks of:{Student_Total_marks}')

percentage = (Student_Total_marks/600)*100

print(f'{Student_name} percentage of :{percentage}')

