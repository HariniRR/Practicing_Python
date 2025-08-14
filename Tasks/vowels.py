#counting vowels
sample=input("Enter a string: ")
vowel=('a','e','i','o','u','A','E','I','O','U')
count=0
for i in range(0,len(sample)):
    if sample[i] in vowel:
        count+=1
print(count)
'''op
Enter a string: Unique
4 '''
