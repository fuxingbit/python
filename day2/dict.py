#Author: Jenliver

info = {
    'str1':"zjn",
    'str2':"zjning",
    'str3':"Jenliver",
    'str4':"Alien",
}
i = {
    'str1':"edcvfr",
    1:3
}
'''
#print(info)
#info['str4'] = "aliensss"
#info['str5'] = "alienxxx"
print(info['str4'])
print(info.get('str2'))   #安全的获取，不报错

print('str3' in info)     #判断在不在字典里
#del info['str1']
#info.pop("str3")
#info.popitem()  #随机删
print(info)
'''

#多级字典的嵌套及操作

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"

av_catalog.setdefault("feizhou", {"www.baidu.com":[1, 2]})
print(av_catalog)

c = dict.fromkeys([6, 7, 8], "test")    #初始化一个字典

info.update(i)
print(info)             #合并2个字典，已经有的更新，没有的新建
print(info.items())     #将字典转成列表

#遍历字典
for i in info:
    print(i, info[i])
#效率不如上面的高
for k, v in info.items():
    print(k, v)