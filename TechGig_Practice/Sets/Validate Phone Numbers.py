'''In the country of Utopia, Phones Numbers starts with the digit 1 or 2 followed by exactly 12 digits i.e Phones Numbers comprises of 13 digits.
Now, Given N numbers you have to check, whether they are Valid or Invalid.
If they are Valid, print Valid" otherwise print "Invalid".'''
def main():
    n = int(input())
    for _ in range(n):
        number = input().strip()
        if len(number) == 13 and number[0] in ('1', '2') and number.isdigit():
            print("Valid")
        else:
            print("Invalid")

main()