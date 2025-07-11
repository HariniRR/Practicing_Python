a = list(map(int, input("Enter an array: ").split()))
b=int(input("enter a number"))
c=0
for i in a:
    if i<b:
        c+=1
print (c)
#number of element in the array less than b
