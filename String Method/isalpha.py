word = "Hello"
if word.isalpha():
    print(f"'{word}' contains only alphabetic characters.")
else:
    print(f"'{word}' contains non-alphabetic characters.")

# output : 'Hello' contains only alphabetic characters.


word = "Hello123"
if word.isalpha():
    print("Only letters!")
else:
    print("Contains non-letter characters.")

#output : Contains non-letter characters.