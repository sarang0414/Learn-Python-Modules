import re

# Phone number should be in format code-0123456789

phone = "91-7894561230 9656262 1-82626294 1-0123456789"

valid_num = re.findall("\d{0,3}-\d{10}",phone)
print(valid_num)