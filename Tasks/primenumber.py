#printing prime nums from 1 to 100
print("2 \n3 \n5 \n7")
for i in range(11,100) :
    if(i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0 ):
        print(i)
        i=i+1
'''op
2 
3 
5 
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

from sympy import primerange
print(list(primerange(1, 101)))

'''
