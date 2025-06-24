empty_tuple = ()  
single_item_tuple = (42,)  
fruits = ('apple', 'banana', 'cherry', 'date')  
mixed_tuple = (1, 'a', 3.14, True)  # A tuple with mixed data types

#Display the created tuples
print("Single item tuple:", single_item_tuple)
print("Fruits tuple:", fruits)
print("Mixed tuple:", mixed_tuple)

#Accessing elements
print("First fruit:", fruits[0])  
print("Last fruit:", fruits[-1]) 
print("Slice (1:3):", fruits[1:3]) 

#Tuple operations
double_fruits = fruits * 2  # Repeat the tuple
more_fruits = fruits + ('elderberry', 'fig')  # Concatenate another tuple
print("Repeated tuple:", double_fruits)
print("Concatenated tuple:", more_fruits)

#Built-in functions
print("Length:", len(fruits)) 
print("Count of 'apple':", fruits.count('apple'))  
print("Index of 'cherry':", fruits.index('cherry'))  
print("Max value:", max((3, 1, 4, 1, 5)))
print("Min value:", min((3, 1, 4, 1, 5)))  
print("Sorted tuple view:", tuple(sorted(fruits + ('apple',)))) 
print("Any true?", any((0, False, 1)))  
print("All true?", all((1, True, 'a')))

#Tuple unpacking
a, b, c, d = fruits  # Unpack the tuple into variables
print("Unpacked: a=", a, ", b=", b, ", c=", c, ", d=", d)
first, *middle, last = fruits  # Extended unpacking
print("Extended unpacking: first=", first, ", middle=", middle, ", last=", last)

#Tuple comparison
print("\n6. Tuple Comparison:")
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print("Comparison (t1 < t2):", t1 < t2)  # Compare tuples element by element

#Checking membership=
print("'banana' in fruits:", 'banana' in fruits)  
print("'grape' not in fruits:", 'grape' not in fruits) 

#Nested tuples
nested = ((1, 2), (3, 4), (5, 6)) 
print("Nested tuple:", nested)
print("First element of second tuple:", nested[1][0])  

#Zip and enumerate (returning tuple views)
numbers = (1, 2, 3)
letters = ('a', 'b', 'c')
zipped = tuple(zip(numbers, letters))  # Combine two tuples into a tuple of pairs
enumerated = tuple(enumerate(fruits))  # Enumerate the fruits tuple
print("Zipped:", zipped)
print("Enumerated:", enumerated)


"""
Remember: Tuples are immutable! 
These operations DON'T modify the original tuple but return new tuples.
tuple.methods: dict_keys(['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__len__', '__getitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__getnewargs__', 'index', 'count', '__class_getitem__', '__doc__'])
-commoon functions are
    count(), index(), len(), max(), min(), sum(), any(), all(), sorted(), tuple()

output
Single item tuple: (42,)
Fruits tuple: ('apple', 'banana', 'cherry', 'date')
Mixed tuple: (1, 'a', 3.14, True)
First fruit: apple
Last fruit: date
Slice (1:3): ('banana', 'cherry')
Repeated tuple: ('apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'date')
Concatenated tuple: ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig')
Length: 4
Count of 'apple': 1
Index of 'cherry': 2
Max value: 5
Min value: 1
Sorted tuple view: ('apple', 'apple', 'banana', 'cherry', 'date')
Any true? True
All true? True
Unpacked: a= apple , b= banana , c= cherry , d= date
Extended unpacking: first= apple , middle= ['banana', 'cherry'] , last= date

6. Tuple Comparison:
Comparison (t1 < t2): True
'banana' in fruits: True
'grape' not in fruits: True
Nested tuple: ((1, 2), (3, 4), (5, 6))
First element of second tuple: 3
Zipped: ((1, 'a'), (2, 'b'), (3, 'c'))
Enumerated: ((0, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'date'))


"""
