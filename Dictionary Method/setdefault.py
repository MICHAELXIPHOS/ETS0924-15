person = {'name': 'Alice', 'age': 25}

# Key exists - returns current value
age = person.setdefault('age', 30)
print(age)  # Output: 25

# Key doesn't exist - adds key with default value and returns it
city = person.setdefault('city', 'New York')
print(city)  # Output: New York
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}