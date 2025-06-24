#my_dict = {}
tree_heights = {
    'neem': 15,
    'banyan': 20,
    'mango': 10,
    'peepal': 18
}
print("Original dictionary:", tree_heights)

# Accessing values
print("Height of mango tree:", tree_heights['mango'])

# Adding new key-value pair
tree_heights['gulmohar'] = 12
print("After adding gulmohar:", tree_heights)

# Updating a value
tree_heights['mango'] = 11
print("After updating mango height:", tree_heights)

# Using get()
print("Get height of teak:", tree_heights.get('teak'))  # None
print("Get height of teak with default:", tree_heights.get('teak', 'Not available'))

# Using setdefault()
tree_heights.setdefault('teak', 17)
print("After setdefault for teak:", tree_heights)
tree_heights.setdefault('banyan', 30)
print("After setdefault for existing key banyan (no change):", tree_heights)

# Removing elements
removed = tree_heights.pop('neem')
print("After popping neem:", tree_heights, "| Removed:", removed)

last_item = tree_heights.popitem()  # Removes the last inserted key-value pair
print("After popitem:", tree_heights, "| Removed item:", last_item)

del tree_heights['peepal']
print("After deleting peepal:", tree_heights)

# Updating dictionary with another dictionary
extra_heights = {'sal': 14, 'birch': 9}
tree_heights.update(extra_heights)
print("After updating with extra_heights:", tree_heights)

# fromkeys()
new_trees = dict.fromkeys(['pine', 'cedar', 'elm'], 8)
print("New dictionary from fromkeys():", new_trees)

# keys(), values(), items()
print("All keys:", list(tree_heights.keys()))
print("All values:", list(tree_heights.values()))
print("All items:", list(tree_heights.items()))

# Copying
copied_dict = tree_heights.copy()
print("Copied dictionary:", copied_dict)

# Checking existence
print("Is 'sal' in dictionary?", 'sal' in tree_heights)
print("Is 'maple' not in dictionary?", 'maple' not in tree_heights)

# Clearing
tree_heights.clear()
print("After clearing tree_heights:", tree_heights)

"""
Note:
- Dictionaries store key-value pairs and are mutable.
- Keys must be unique and immutable (e.g., strings, numbers, tuples).
- Values can be of any data type.
- Dictionaries preserve insertion order (Python 3.7+).
- Use get(key) or setdefault(key) to avoid KeyError for missing keys.
- Common dictionary functions:
    get(), setdefault(), update(), keys(), values(), items(), pop(), popitem(), clear(), copy(), fromkeys(), del, in, len(), keys(), values(), items()


  op
Original dictionary: {'neem': 15, 'banyan': 20, 'mango': 10, 'peepal': 18}
Height of mango tree: 10
After adding gulmohar: {'neem': 15, 'banyan': 20, 'mango': 10, 'peepal': 18, 'gulmohar': 12}
After updating mango height: {'neem': 15, 'banyan': 20, 'mango': 11, 'peepal': 18, 'gulmohar': 12}
Get height of teak: None
Get height of teak with default: Not available
After setdefault for teak: {'neem': 15, 'banyan': 20, 'mango': 11, 'peepal': 18, 'gulmohar': 12, 'teak': 17}
After setdefault for existing key banyan (no change): {'neem': 15, 'banyan': 20, 'mango': 11, 'peepal': 18, 'gulmohar': 12, 'teak': 17}
After popping neem: {'banyan': 20, 'mango': 11, 'peepal': 18, 'gulmohar': 12, 'teak': 17} | Removed: 15
After popitem: {'banyan': 20, 'mango': 11, 'peepal': 18, 'gulmohar': 12} | Removed item: ('teak', 17)
After deleting peepal: {'banyan': 20, 'mango': 11, 'gulmohar': 12}
After updating with extra_heights: {'banyan': 20, 'mango': 11, 'gulmohar': 12, 'sal': 14, 'birch': 9}
New dictionary from fromkeys(): {'pine': 8, 'cedar': 8, 'elm': 8}
All keys: ['banyan', 'mango', 'gulmohar', 'sal', 'birch']
All values: [20, 11, 12, 14, 9]
All items: [('banyan', 20), ('mango', 11), ('gulmohar', 12), ('sal', 14), ('birch', 9)]
Copied dictionary: {'banyan': 20, 'mango': 11, 'gulmohar': 12, 'sal': 14, 'birch': 9}
Is 'sal' in dictionary? True
Is 'maple' not in dictionary? True
After clearing tree_heights: {}

"""
