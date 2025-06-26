'''You just need to take two number as input from stdin and you need to find prime numbers between those two numbers and print them.

Input Format
You will be taking two numbers as an input from stdin one on each line respectively.

Constraints
1 <= N <= 10000

Output Format
You need to print the prime numbers one on each line to the stdout.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    if is_prime(i):
        print(i)
