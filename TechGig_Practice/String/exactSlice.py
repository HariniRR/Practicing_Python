# take string input and two other numbers which will be the start and end point of the slice and you need to print that slice of string to the stdout.
def main():
    ins=input().strip()
    st=int(input())
    en=int(input())
    print(ins[st:en+1])
 # Write code here 

main()
