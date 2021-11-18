import re

def make_slug(str1):
    if str1[0]==' ' or str1[-1]== ' ':
        var1 = re.sub(" ","-",str1[1:-2:1])
    else:
        var1 = re.sub(" ","-",str1)
    print(var1)

str1 = input("Enter String :")
make_slug(str1)