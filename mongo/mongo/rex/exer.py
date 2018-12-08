import re

f = open('note.txt')
data = f.read()

# pattern = r'\b[A-Z]\S*'
pattern = r'-?\d+\.?/?\d*%?'

l = re.findall(pattern,data)
print(l)
f.close()
