import re

# Input from user
password = input("Enter password: ")

# Regex pattern
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*]).{8,}$'

# Validation
if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")