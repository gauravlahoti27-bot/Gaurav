import re

# Input string
text = "man mango map cat mobile mouse dog"

# Find words starting with 'm'
result = re.findall(r'\bm\w*', text)

print("Words starting with 'm':", result)