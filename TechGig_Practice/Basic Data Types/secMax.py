#The marks of Ranu are given in N subjects and you have to tell him the second maximum marks he has got.Marks may or may not duplicate.
def main():
    n=int(input())
    mark=list(map(int,input().split()))
    m=max(mark)
    mark = [x for x in mark if x != m]
    print(max(mark))

 # Write code here 

main()

''' mark.sort(reverse=True)  # Sort descending
    max_val = mark[0]
    for x in mark:
        if x < max_val:
            print(x)
            break '''