import re

num = "12 , 123 , 1234 , 123456 , 1234567 , 123456789"
data = re.findall(r'\d{5,8}',num)
print(data)

str = "sat pat mat lat cat"
data1 = re.findall(r'[p-z]at',str)
print(data1)
print(re.findall(r'[^p-z]at',str))

str1 = "j jnson j \\dbhb"
data2 = re.search(r'\\dbhb',str1)
print(str1)
print(data2)

if re.search("\w{2,20}\s\w{2,20}","Sarang Krishna"):
    print("its a valid Full Name")

phone = "444-212-2142"
if re.search("\d{3}-\d{3}-\d{4}",phone):
    print("Phone number %(phone)s is valid" %{'phone':phone})

email = "user.l@gmail.com hwq@mwk.com nwj.com   kwjno@ji"
valid_email = re.findall("[\w._+*]{2,20}@[\w._+%*]{2,6}.[a-zA-Z]{2,7}",email)
print(valid_email)
