# program that checks if a number is even or odd. Use an if statement for the condition.
num=int(input("Enter a positive integer: "))
if(num<0) :
    print("Invalid Input")
elif(num%2==0):
    print("Even number")
else:
    print("Odd number")
'''output
Enter a positive integer: 22
Even number
'''
