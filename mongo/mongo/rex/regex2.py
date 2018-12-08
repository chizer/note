import re

pattern = r'(ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

#获取match
obj = regex.search('abcdefgh')

#obj属性变量
print(obj.pos)      #目标字串开始位置
print(obj.endpos)   #结束位置
print(obj.re)       #正则
print(obj.string)   #目标字串
print(obj.lastgroup)    #最后一组名称
print(obj.lastindex)    #最后一组序号
print('='*20)
print(obj.span())
print(obj.start())
print(obj.end())

print(obj.group())  #获取正则匹配到的内容
print(obj.group(1)) #获取第一组对应内容
print(obj.group('dog')) #获取dog组对应的内容

print(obj.groupdict())  #捕获组字典，只显示捕获组
print(obj.groups())     #所有子组对应内容