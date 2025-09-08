'''Collections module implements specialized container datatypes providing alternatives to Python s general purpose built-in containers, dict, list, set, and tuple.
A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
Your task is to find the top two most recurring characters in a given string using most_common() function of the module.'''
from collections import Counter

def main():
    s = input()
    counter = Counter(s)
    top_two = counter.most_common(2)
    print(top_two[0], top_two[1])

main()