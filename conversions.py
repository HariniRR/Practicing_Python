# Sample data
sample_list = [1, 2, 3, 4]
sample_tuple = (5, 6, 7, 8)
sample_set = {9, 10, 11, 12}
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# List conversions
tuple_from_list = tuple(sample_list)
set_from_list = set(sample_list)

# Tuple conversions
list_from_tuple = list(sample_tuple)
set_from_tuple = set(sample_tuple)

# Set conversions
list_from_set = list(sample_set)
tuple_from_set = tuple(sample_set)

# Dict conversions
keys_list = list(sample_dict.keys())
values_list = list(sample_dict.values())
items_list = list(sample_dict.items())

keys_tuple = tuple(sample_dict.keys())
values_tuple = tuple(sample_dict.values())

# List of pairs to dict
pairs_list = [('x', 100), ('y', 200)]
dict_from_pairs = dict(pairs_list)

# From set of pairs to dict
set_of_pairs = {('m', 1), ('n', 2)}
dict_from_set_of_pairs = dict(set_of_pairs)

# Display all results
print("Tuple from list:", tuple_from_list)
print("Set from list:", set_from_list)

print("List from tuple:", list_from_tuple)
print("Set from tuple:", set_from_tuple)

print("List from set:", list_from_set)
print("Tuple from set:", tuple_from_set)

print("Dict keys to list:", keys_list)
print("Dict values to list:", values_list)
print("Dict items to list:", items_list)

print("Dict keys to tuple:", keys_tuple)
print("Dict values to tuple:", values_tuple)

print("Dict from list of pairs:", dict_from_pairs)
print("Dict from set of pairs:", dict_from_set_of_pairs)
