import re

# Input from user
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

# Phone number pattern (10 digits, starts with 6-9)
phone_pattern = r'^[6-9]\d{9}$'

# Email pattern
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validation
if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

if re.match(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
