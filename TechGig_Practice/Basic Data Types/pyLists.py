''' Your task is to maintain a list and perform two types of queries on it : 
Query '1' : It will be given as 1 x  : Insert x into the list.
Query '2' : It will be given as 2 : Print the contents of the list.
ip:5
1 32
2
1 arpit
1 54
2
op:['32']
['32', 'arpit', '54']'''

def main():
    Q = int(input())
    lst = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            lst.append(query[1])
        elif query[0] == '2':
            print(lst)

main()