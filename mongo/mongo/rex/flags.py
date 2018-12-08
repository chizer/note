import re

s= '''hello world
nihao bejing
'''
pattern = r'^nih'


regex = re.compile(pattern,re.M)

try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)