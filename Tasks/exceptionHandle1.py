#Write a program that takes two numbers as input and divides them. Handle the case where the second number is zero by printing an error message
num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2st number: '))
try:
    res=num1 / num2
    print('Result', res)
    res1=num2 / 0
    print('Result', res1)
except ZeroDivisionError:
    print('Error occurs: Zero division error')
else:
    print('No exception raised')
finally:
    print('This is Finally Block')
'''op
Enter 1st number: 8
Enter 2st number: 6
Result 1.3333333333333333
Error occurs: Zero division error
This is Finally Block
'''
