username = "User123"
if username.isalnum():
    print("Valid username.")
else:
    print("Username must contain only letters and numbers.")


print("  abc  ".isspace())  # False
print("\n\t ".isspace())    # True (newline, tab, space)
print("".isspace())         # False (empty string)