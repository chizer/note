import re
import sys

num = int(sys.argv[1]) 
print(num)

f =open('1.txt','r')
data = f.read()

pattern = r'(BIV1).+\s+(\d+\.+\d+\.+\d+\.+\d+/?\d+)'
dl = re.findall(pattern,data)
print(dl)
f.close()