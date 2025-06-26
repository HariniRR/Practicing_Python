empty_set = set()
my_set = {'neem', 'banyan', 'mango'}
mixed_set = {1, 'oak', 3.14, True}

print("Empty set:", empty_set)
print("My set:", my_set)
print("Mixed set:", mixed_set)

my_set.add('peepal')
print("After adding 'peepal':", my_set)
my_set.update(['gulmohar', 'teak'])
print("After update:", my_set)

my_set.remove('banyan')  # Raises error if not found
print("After removing 'banyan':", my_set)
my_set.discard('palm')  # Does not raise error if not found
print("After discarding 'palm':", my_set)
popped = my_set.pop()  # Removes a random element
print("After popping one element:", my_set, "| Popped:", popped)

a = {'neem', 'mango', 'teak', 'oak'}
b = {'teak', 'oak', 'pine', 'cedar'}
print("Set a:", a)
print("Set b:", b)
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))

a.difference_update(b)
print("After a.difference_update(b):", a)

immutable_trees = frozenset(['neem', 'mango', 'bamboo'])
print("Frozen set:", immutable_trees)

print("'mango' in b?", 'mango' in b)
print("'sal' not in b?", 'sal' not in b)

print("Is b subset of b?", b.issubset(b))
print("Is b superset of a?", b.issuperset(a))
print("Are a and b disjoint?", a.isdisjoint(b))

tree_heights = {15, 25, 10, 30}
print("Tree heights set:", tree_heights)
print("Length:", len(tree_heights))
print("Max:", max(tree_heights))
print("Min:", min(tree_heights))
print("Sum:", sum(tree_heights))
print("Any true?", any(tree_heights))
print("All true?", all(tree_heights))

list_to_set = set(['birch', 'elm', 'birch', 'maple'])
print("Converted from list:", list_to_set)
copied_set = my_set.copy()
print("Copied set:", copied_set)

my_set.clear()
print("After clearing:", my_set)

"""
Note:
- Sets are unordered, so indexing/slicing is not supported.
- Sets are mutable, but all elements must be immutable.
- Sets automatically remove duplicates.
- Use discard(element) to remove an item without raising an error if it doesn't exist.
- frozenset() creates an immutable version of a set.
- difference_update(other_set) removes elements found in another set from the original set.
- update_update
- symmetric_difference_update
- join()
Common set functions
     get(), setdefault(), update(), keys(), values(), items(), pop(), popitem(), clear(), copy(), fromkeys(), del, len()


output
Empty set: set()
My set: {'neem', 'mango', 'banyan'}
Mixed set: {1, 3.14, 'oak'}
After adding 'peepal': {'neem', 'mango', 'peepal', 'banyan'}
After update: {'mango', 'banyan', 'peepal', 'gulmohar', 'neem', 'teak'}
After removing 'banyan': {'mango', 'peepal', 'gulmohar', 'neem', 'teak'}
After discarding 'palm': {'mango', 'peepal', 'gulmohar', 'neem', 'teak'}
After popping one element: {'peepal', 'gulmohar', 'neem', 'teak'} | Popped: mango
Set a: {'neem', 'mango', 'teak', 'oak'}
Set b: {'pine', 'teak', 'oak', 'cedar'}
Union: {'pine', 'mango', 'oak', 'cedar', 'neem', 'teak'}
Intersection: {'teak', 'oak'}
Difference (a - b): {'neem', 'mango'}
Symmetric Difference: {'pine', 'mango', 'cedar', 'neem'}
After a.difference_update(b): {'neem', 'mango'}
Frozen set: frozenset({'neem', 'mango', 'bamboo'})
'mango' in b? False
'sal' not in b? True
Is b subset of b? True
Is b superset of a? False
Are a and b disjoint? True
Tree heights set: {25, 10, 30, 15}
Length: 4
Max: 30
Min: 10
Sum: 80
Any true? True
All true? True
Converted from list: {'birch', 'maple', 'elm'}
Copied set: {'neem', 'teak', 'peepal', 'gulmohar'}
After clearing: set()

"""
