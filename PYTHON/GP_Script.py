import re

phone_pattern = r'^[6-9]\d{9}$'
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if re.match(email_pattern,email):
    print("Valid email address")
else:
    print("Invalid email address")