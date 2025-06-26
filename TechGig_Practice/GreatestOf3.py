'''You just need to take three number as input from stdin and you need to find greatest of them.

Input Format
You will be taking three numbers as an input from stdin one on each line respectively.

Constraints
-100000 <= N <= 100000

Output Format
You need to print the greatest of the three numbers to the stdout.'''
def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    print(max(num1,num2,num3))
 # Write code here 

main()