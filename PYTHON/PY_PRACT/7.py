import re
text = "pear plum pages play pairs pin paint part pac"

pattern = re.findall(r'\bp\w{2,3}\b',text)
print(pattern)