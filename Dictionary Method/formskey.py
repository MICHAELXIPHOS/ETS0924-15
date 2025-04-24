# Create a list of keys
keys = ['name', 'age', 'city']

# Create a dictionary with all values set to 'Unknown'
default_value = 'Unknown'
person_info = dict.fromkeys(keys, default_value)

print(person_info)
