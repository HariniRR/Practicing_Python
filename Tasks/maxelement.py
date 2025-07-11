arr=list(map(int,input("Enter an array:").split()))
max=0
for i in arr:
    if i>max:
        max=i
print("maximum element in the array:",max)
