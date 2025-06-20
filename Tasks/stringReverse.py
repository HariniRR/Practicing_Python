#program that takes a string as input and returns the string in reverse order.
original = input("Enter a string to reverse: ")
reversed_str = ""
index = len(original) - 1

while index >= 0:
    reversed_str += original[index]
    index -= 1
'for i in range(len(original) - 1, -1, -1):'
    'reversed_str += original[i]'
    
print("Reversed string:", reversed_str)
print("Reversed string",original[::-1])
'''op
Enter a string to reverse: division
Reversed string: noisivid
Reversed string noisivid
'''
