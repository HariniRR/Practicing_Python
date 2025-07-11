str = input("Enter a string:")
letter = input("Enter a letter:")[0]
vowels = "aeiouAEIOU"
count = 0
has_uppercase = False
word_count = 0
in_word = False
space_count = 0
max_word = ""
letter_count = 0
word = ""
char_count = {}
has_digit = False

#counting number of vowels
for char in str:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

#if string contains uppercase letter
for char in string:
    if 'A' <= char <= 'Z':
        has_uppercase = True
        break
if has_uppercase:
    print("The string contains uppercase letters.")
else:
    print("The string does not contain uppercase letters.")

#count of number of words
for char in string:
    if char.isalpha():  # to ignore white spaces
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False
print("Number of words:", word_count)

#counting number of white spaces
for char in string:
     if char.isspace():  # to ignore white spaces
            space_count += 1
print("Number of words:", space_count + 1)

#largest word in the str
for char in str:
    if char.isspace():
        if len(word) > len(max_word):
            max_word = word
        word = ""
    else:
        word += char
if len(word) > len(max_word):
    max_word = word
print("Largest word:", max_word)

#occurance of specific character
for char in str:
    if char == letter:
        letter_count += 1
print("number of ",letter," in the string:", letter_count)

#first repeated character
for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
 print("First repeated character:", char)

 #has numeric digits
for char in str:
    if '0' <= char <= '9':
        has_digit = True
        break
if has_digit:
    print("The string contains at least one numeric digit.")
else:
    print("The string does not contain any numeric digits.")
