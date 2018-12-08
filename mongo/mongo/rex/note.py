import re

word_pattern = r'\b[A-Z]\w+\b'
num_pattern = r"\-?\d+(\d+?\%?|.\d+\%?)?"
f = open('note.txt','r')
string = f.read()
f.close
# print(string)
regex = re.compile(word_pattern)
Word_list = regex.findall(string)
print(Word_list)

regex = re.compile(num_pattern)
num_obj = regex.finditer(string)
for i in num_obj:
    print(i.group())
