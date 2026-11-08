import re

email = "joy@gmail.com"
phone = "01712345678"

if re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(r'^01[3-9]\d{8}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")