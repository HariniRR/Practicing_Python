#prime num using functions
def isprime(n):
    if n <= 1:
        return "not a Prime number"
    for i in range(2, n):
        if n % i == 0:
            return "not a Prime number"
    return "Prime number"

i=int(input("Enter a number: "))
print(isprime(i))

'''op
Enter a number: 98
not a Prime number

Enter a number: 67
Prime number '''
