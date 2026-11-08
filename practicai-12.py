import re

text = "My  number is 12345"

result = re.search("Python", text)

if result:
    print("Pattern Found")
else:
    print("Pattern Not Found")