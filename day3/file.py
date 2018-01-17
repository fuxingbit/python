#Author: Alienzjn

# open file
# data = open("yesterday", encoding="utf-8").read()
# f = open("yesterday", 'rw', encoding="utf-8")   # 文件句柄
# data = f.read()
# print(data)

#w = open("day2", 'w', encoding="utf-8")
# w.write("人生苦短，我用python\n")
# w.write("人生苦短，我用python")

#a = append追加
# w = open("day2", 'a', encoding="utf-8")
# w.write("\n人生苦短，我用python\n")
# w.write("人生苦短，我用python尜尜")

f = open("yesterday2", 'w', encoding="utf-8")

# f.write("hello 1\n")
# f.write("hello 2\n")
# f.write("hello 3\n")


# print(f.readlines())

# for line in f.readlines():
#     print(line.strip())


# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print ("-------------我是分割线-----------------")
#         continue
#     print(line.strip())

# count = 0
# for line in f:
#     if count == 9:
#         print("-------------我是分割线-----------------")
#         count += 1
#         continue
#     print(line)
#     count += 1


# 打印光标位置，按字符计数
#print(f.tell())
# print(f.read(10))
#print(f.readline())
#print(f.tell())

# 返回光标
#f.seek(9)
#print(f.readline())

# 文件字符编码
#print(f.encoding)

# 刷新，写完刷到硬盘上
#print(f.flush())

#for i in range(5):
#    print(f.readline())

