#Mylist=['orange','guava','banana','peach','berry','apple','cherry']
#Mylist=[]
#mylist=list()

my_list=list()
my_list.append(16)
my_list.append(37)
my_list.append(20)
my_list.append(52)
my_list.append(67)
my_list.append(44)  #insert()
my_list.insert(0, 5)  # Inserts 5 at index 0

print("Original list 2:", my_list)
print("Reversing the list:", my_list[::-1])

my_list1 = [45, 25, 57, 26]
print("Count of the element '20':", my_list.count(20))
print("Length of the list:", len(my_list))
my_list.extend(my_list1)
print("adding 2 lists:", my_list)
print("Length of the list after adding:", len(my_list))

print("Slicing", my_list[1:6:5])
print("Sorted list 1:", my_list.sort())
print("Reversing Sorted list:", my_list.reverse())
print("Index of '25':", my_list.index(25))

#remove(value)
#pop(index)
#del list[index] or del list[start:end]: Deletes elements by index or a slice.
print("Pop:", my_list.pop(4))
print("Remove:", my_list.remove(45))
del my_list[5]
print("Delete:", my_list)

print("maximum element in the list:", max(my_list))
print("minimum element in the list:", min(my_list))
print("sum of the element in the list:", sum(my_list))
print("Are all the elements true in the list?:", all(my_list))
print("Is any element true in the list?:", any(my_list))
print("enumerating my_list, (index,value):", list(enumerate(my_list)))

#print(,my_list.zip())  Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.

my_list.clear()  #copy()
print("Is the list empty?", len(my_list) == 0)

"""
Note:
- Lists are ordered, so indexing and slicing are supported.
- Lists are mutable, meaning you can modify, add, or remove elements.
- Lists can contain duplicate elements.
- Elements in a list can be of different data types (heterogeneous).
- Lists preserve the insertion order.
- common list functions
# append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), len(), max(), min(), sum(), any(), all(), list()
"""


'''op
Original list 2:  [5, 16, 37, 20, 52, 67, 44]
Reversing the list:  [44, 67, 52, 20, 37, 16, 5]
Count of the element'20':  1
Length of the list:  7
adding 2 lists:  [5, 16, 37, 20, 52, 67, 44, 45, 25, 57, 26]
Length of the list after adding:  11
Slicing  [16]
Sorted list 1:  None
Reversing Sorted list:  None
Index of '25':  7
Pop:  44
Remove:  None
Delete:  [67, 57, 52, 37, 26, 20, 16, 5]
maximum element in the list:  67
minimum element in the list:  5
sum of the element in the list:  280
Are all the elements true in the list?:  True
Is any element true in the list?:  True
enumerating  my_list, (index,value):  [(0, 67), (1, 57), (2, 52), (3, 37), (4, 26), (5, 20), (6, 16), (7, 5)]
Is the list empty? True
'''
