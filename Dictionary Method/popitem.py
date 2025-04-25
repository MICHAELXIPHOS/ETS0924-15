# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove and return the last item
last_item = my_dict.popitem()

print("Removed item:", last_item)  # Output: ('c', 3)
print("Updated dictionary:", my_dict)  # Output: {'a': 1, 'b': 2}