__author__ = "Jenliver"
__date__ = "2017/09/09"

import sys

f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday2.new","w",encoding="utf-8")

# for line in f:
#     if "hello" in line:
#         line = line.replace("hello","hello world")
#     f_new.write(line)
# f.close()
# f_new.close()


find_str = sys.argv[1]
replace_str = sys.argv[2]

for line in f:
    if find_str in line:
        line = line.replace(find_str,replace_str)
    f_new.write(line)
f.close()
f_new.close()





