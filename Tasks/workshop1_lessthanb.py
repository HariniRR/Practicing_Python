#num of elements in an array that are < a specific num 
#a=list(map(int(input("enter an array").split())))
a = []
v = list(map(int, input("Enter an array: ").split()))
a.append(v)
b=int(input("enter a number"))
c=0
for i in a:
    if i<b:
        c+=1
print (c)
