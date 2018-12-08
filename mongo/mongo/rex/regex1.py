import re

pattern = r'\d+'
s = '2018年,08奥运会,512地震'

it = re.finditer(pattern,s)


# for i in it :
#     print(i)
#     print(i.group())
# print(dir(i))
try:
    obj = re.match(r'[a-z]\w+','hello24')    
    print(obj.group())
except AttributeError as e:
    print(e)