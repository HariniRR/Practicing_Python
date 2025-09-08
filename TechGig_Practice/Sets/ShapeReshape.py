'''The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array. 
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
Now, Given 9 Integers, You have to convert them into 3*3 Numpy array using Reshape function.'''
import numpy as np

def main():
    arr = list(map(int, input().split()))
    reshaped = np.array(arr).reshape(3, 3)
    print(reshaped)

main()

''' without numpy,
def main():
    arr = list(map(int, input().split()))
    print("[", end="")
    for i in range(0, 9, 3):
        row = arr[i:i+3]
        print("[" + " ".join(map(str, row)) + "]", end="")
        if i < 6:
            print("\n ", end="")
    print("]")

main()'''
