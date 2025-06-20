# a program that takes a list of integers and returns a new tuple containing only the even numbers.
mylist=list(map(int,input("Enter a list: ").split()))
myevenlist=list()
for i in mylist:
    if(i%2 == 0):
        myevenlist.append(i)
mytuple=tuple(myevenlist)
print("Even tuple: ",mytuple)
'''op
Enter a list: 10 4 5 8 9 7 45 78 66 55 21 3 45 11 78
Even tuple:  (10, 4, 8, 78, 66, 78)
'''
