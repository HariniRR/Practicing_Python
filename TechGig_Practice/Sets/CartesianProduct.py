'''For sets A and B, the Cartesian product of A and B, denoted AxB, is the set of all ordered pairs (a, b) such that a A and b B. That is, AxB = {(a, b)| a A b B}. 
itertools.product() computes the cartesian product of input iterables. 
 For example, product(P, Q) returns the same as ((x,y) for x in P for y in Q). 
You are given a two lists A and B. Your task is to compute their cartesian product AXB.'''
from itertools import product

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = product(A, B)
    print(' '.join(str(t) for t in result))

main()