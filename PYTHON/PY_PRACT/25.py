import re

# Input from user
url = input("Enter URL: ")

# Regex pattern for URL validation
pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[\w\-./?%&=]*)?$'

# Validation
if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")
    
