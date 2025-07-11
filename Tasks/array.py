arr = list(map(int,input("Enter an array:").split()))
num=int(input("Enter a number:"))
max = 0
sum = 0
s = 0
count = 0
c = 0
d_odd = 0
t_odd = 0
mini = arr[0]
neg_num = None
sq_sum = 0
 first_perfect_square = None

#maximum element
for i in arr:
    if i>max:
        max=i
print("maximum element in the array:",max)

#number of even numbers
for i in arr:
    if i%2 == 0:
        count += 1
        s += i
print("sum of even numbers:",s)
print("number of even numbers:",count)

#sum of positive numbers
for i in arr:
    if i > 0:
        sum += i
print("sum of positive element in the array:",sum)

#minimum element
for i in arr:
    if i < mini:
        mini = i
print("minimum element in the array:",mini)

#count occurance of a specific number num
for e in arr:
        if e == num:
            c += 1
print("number of",num,"in the array:",c)

#number of odd numbers
for i in arr:
    if i%2 != 0:
        d_odd = 0 += 1
        t_odd = 0 += i
print("sum of odd numbers:",t_odd = 0)
print("number of odd numbers:",d_odd = 0)

#first negative number
for i in arr:
    if i < 0:
        neg_num = i
        break
print("First negative number:",neg_num)

#sum of squares of element 
for i in arr:
    q = i*i
    sq_sum += q
print("sum of squares of elements:",sq_sum)

#first perfect square
for i in arr:
    root = int(i ** 0.5)
    if root * root == i:
        first_perfect_square = i
        break

print("First perfect square is:",first_perfect_square)