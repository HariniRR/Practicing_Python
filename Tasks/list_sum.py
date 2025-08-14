#read list to return the sum of items
mylist=list(map(int,input("Enter a list of nums: ").split()))
sum=0
i=len(mylist)-1
while(i != -1): # i < len(mylist): i+=1
    sum+=mylist[i]
    i-=1
print("Sum of elements in the list is ",sum)
'''opEnter a list of nums: 2 4 8 6 3 7 5 9
Sum of elements in the list is  44'''
