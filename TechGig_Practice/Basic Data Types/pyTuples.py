'''You are given N Integers. Your task is to create a tuple and insert all the given integers into it.
After insertion, You have to print the count of a particular element X (total number of occurrence of that element) in the tuple.'''
def main():
    n = int(input())  
    elements = tuple(map(int, input().split()))  
    x = int(input())
    print(elements.count(x))

main()