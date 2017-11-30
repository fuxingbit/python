#Author: Alienzjn

name = "My \tname is alienzjn"

print(name.capitalize())     #首字母大写
print(name.count("n"))       #字符中有2个n
print(name.center(50, "-"))  #
print(name.encode("utf-8"))
print(name.endswith("jn"))          #判断字符串以什么结尾
print(name.expandtabs(tabsize=30))  #把tab键空30格
print(name.find("M"))               #返回字符在字符串中的索引
print(name[name.find("name"):9])

name2 = "my name is {na} and i am {age} old"
print(name2.format(na="zjn", age=22))
print(name2.format_map({'na':'zjn', 'age':12}))
print('ABC112'.isalnum())            #判断是否是数字或字母,包含特殊字符为false
print('ABCss'.isalpha())             #判断是否是纯英文字符
print('1022A'.isdecimal())           #判断是否是十进制
print('102'.isdigit())               #判断是否为整数
print('1naee'.isidentifier())        #判断是否为一个合法的标识符
print('naee'.islower())              #判断是否是小写
print('SSSDFC'.isupper())            #判断是否是大写
print('99.0'.isnumeric())            #判断是否是整数
print('    '.isspace())              #判断是否是空格
print('My Name Is'.istitle())        #判断是否首字母大写
print('My Name Is'.isprintable())    #tty file.drive file
print('+'.join(['1', '2', '3']))
print("sssss".join("::::::"))
print(name.ljust(50, '*'))          #左对齐，长度不够50用*代替
print(name.rjust(50, '-'))          #右对齐，长度不够50用-代替
print('ALen'.lower())               #大写变小写
print('ALen'.upper())               #小写变大写
print('\nALen\n'.lstrip())          #去掉左边的空格和回车
print('\nALen\n'.rstrip())          #去掉右边的空格和回车
print('\n   ALen\n  '.strip())          #去掉空格和回车
p = str.maketrans("acdefg", '123456')
print("acdefg".translate(p))        #替换
print('zjning'.replace('n', 'N', 1))     #替换
print('zjning'.rfind('n'))              #找最右边的值的下标
print('zjn alien'.split())          #将字符串按空格分成列表
print('zjn alien sf in it '.split('i'))          #将字符串按'i'分成列表
print('1+2+3+4+5+6'.split('+'))          #将字符串按'+'分成列表
print('1+2\n3+4\n5+6'.splitlines())          #将字符串按'\n'分成列表
print('zjnZJN'.swapcase())          #将字符串大写换小写，小写换大写
print('zjnZJN'.zfill(30))          #

print('-----')



