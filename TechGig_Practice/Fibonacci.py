'''You just need to take a number as input from stdin which will tell how many terms of the Fibonacci needs to be printed.

Input Format
You will be taking a number as an input from stdin.

Constraints
1 <= N <= 10000

Output Format
You need to print the Fibonacci series separated by space to the stdout.'''

def main():
    n = int(raw_input())  
    a, b = 0, 1
    print a,  
    count = 1
    while count < n:
        print b,  # Print the next Fibonacci number without a newline
        a, b = b, a + b
        count += 1

main()
