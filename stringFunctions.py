original='StringFunctions'
# + concat, *n repeat n times
#slice str[start:end+1:stride(frequency)]

print('slicing: ',original[1:6])
print('capitalize: ',original.capitalize())
print('casefold: ',original.casefold())
print('center function: ',original.center(15))
print('counting \'c\': ',original.count('n'))
print('Byte encoded : ',original.encode())
print('ASCII encoded : ',original.encode('ascii', errors='replace'))
print('EndsWith function: ',original.endswith("ion"))
print('SttartsWith function: ',original.startswith('str'))
print("finding index: ",original.find('ting'))#rfind() returns the highest indes of the substring
print("finding index: ",original.index('ion'))#rindex()
print("Lower: ",original.lower())
print("upper: ",original.upper())
print("Swapcase: ",original.swapcase())
print("Title: ",original.title())
print("Left justification: ",original.ljust(14,'-'))#rjust(grater than str len,'optional')

# isalnum(), isalpha(), isdecimal(), isdigit(), isidentifier(), islower(), isupper(), isnumeric()isprintable(), isspace(), istitle()
originalstr='manipulate\tstrings'
print('replacing tab character with spaces: ',originalstr.expandtabs())
print("Concat: ",original + originalstr)
#print("Concat: ",original.join(originalstr))

''' nums = re.findall(r'\d+', originalstr)
converted_integer = int(numbers[0]) if numbers else None
print('converted_integer: ',converted_integer)
'''
#format,formatmap()
message = f"Here the {originalstr} are used to {originalstr}".format(originalstr,original)
print('formating: ',message)
print(f"Here the {originalstr} are used to {originalstr}")

data = {"name": "RR", "age": 23}#dictionary
formatted_string = "Hi, I am {name} and {age} years old.".format_map(data)
print('formatted_string with dict: ',formatted_string)
print("replacing substring: ",formatted_string.replace("and",", I am"))
print("formatted_string as tuple : ",formatted_string.rpartition(' '))#' ' partition basis of whitespace
#strip(), split(), rstrip(), rsplit(), splitlines(), zfill()

translation_table = str.maketrans("a", "A", "o") #This maps lowercase vowels to uppercase, and removes 'o'
my_string = "characters description"
translated_string = my_string.translate(translation_table)
print('Translation: ',translated_string)

'''op
slicing:  tring
capitalize:  Stringfunctions
casefold:  stringfunctions
center function:  StringFunctions
counting 'c':  3
Byte encoded :  b'StringFunctions'
ASCII encoded :  b'StringFunctions'
EndsWith function:  False
SttartsWith function:  False
finding index:  -1
finding index:  11
Lower:  stringfunctions
upper:  STRINGFUNCTIONS
Swapcase:  sTRINGfUNCTIONS
Title:  Stringfunctions
Left justification:  StringFunctions
replacing tab character with spaces:  manipulate      strings
Concat:  StringFunctionsmanipulate	strings
formating:  Here the manipulate	strings are used to manipulate	strings
Here the manipulate	strings are used to manipulate	strings
formatted_string with dict:  Hi, I am RR and 23 years old.
replacing substring:  Hi, I am RR , I am 23 years old.
formatted_string as tuple :  ('Hi, I am RR and 23 years', ' ', 'old.')
Translation:  chArActers descriptin
'''
