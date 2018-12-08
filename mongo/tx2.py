import re
import sys

def get_address(port):
    f = open('1.txt')
    while 1:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        # print(data)
        if not data:
            f.close()
            return 'Not found the port'
        #匹配首个单词
        try:
            PORT = re.match(r'\S+',data).group()
            # print(PORT)
            # print(type(PORT))
        except Exception as e:
            print(e)
            continue  
        if port == PORT:
            # pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)'
            address = re.search(pattern,data).group(1)
            f.close()
            return address

if __name__ =='__main__':
    port =sys.argv[1]
    print(get_address(port))