import re
text = "HI I AM GAURAV AND I AM LEARNING PYTHON"

pattern =  re.sub(r'GAURAV', r'JOHN', text)
print(pattern)

new_text = text.replace("GAURAV", "DAN").replace("PYTHON", "JAVA")
print(new_text)