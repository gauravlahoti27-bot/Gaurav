import re

with open("Data.txt", "r") as file:
    text = file.read()

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
phone_pattern = r'[6-9]\d{9}\b'
date_pattern = r'\d{2}/\d{2}/\d{4}\b'

email = re.findall(email_pattern, text)
phone = re.findall(phone_pattern, text)
date = re.findall(date_pattern, text)

print("Email addresses:", email)
print("Phone numbers:", phone)
print("Dates:", date)
