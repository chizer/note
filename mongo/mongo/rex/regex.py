import re

pattern = r'(\w+):(\d+)'
s = 'zhang:1993 li:1996'

# s = re.findall(pattern,s)
# print(s)

regex = re.compile(pattern)
l = regex.findall(s)
l = regex.findall(s,pos=0,endpos=12)
print(l)

l = re.split(r'\s+','hello world')
print(l)

s = re.subn(r'\s+', '##', 'hello world nihao beijing')
print(s)