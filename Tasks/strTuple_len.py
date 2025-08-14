#program that takes a tuple of strings and returns a new tuple with the lengths of each string.
iplist = list(map(str, input('Enter strings seperated by , : ').split(', ')))
strings=tuple(iplist)
lengths = tuple(len(s) for s in strings)
print("lengths:{lengths}")
'''opEnter strings seperated by , : Apple, Banana, Mango, Orange, Pineapple, Grapes, Papaya
lengths:(5, 6, 5, 6, 9, 6, 6)'''
