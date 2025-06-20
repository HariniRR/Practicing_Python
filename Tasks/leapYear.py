year=int(input('Enter a year: '))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Leap year')
else:
    print('Not a leap year')
'''op
Enter a year: 2024
Leap year
'''
