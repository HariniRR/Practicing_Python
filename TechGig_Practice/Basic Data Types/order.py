#A list is to made in alphabetical order
def main():
    n=int(input())
    name=[]
    for _ in range(n):
        person=input()
        name.append(person)
    name.sort()
    for n in name:
        print(n)
 # Write code here 

main()