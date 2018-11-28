# @Time    : 2018/9/13 15:28
# @Author  : Jennings
# @Email   : zjn@wiwi.ink


import urllib, re
import urllib.request

# 安装requests,selenium,chromedriver,phantomjs,lxml,beautifulsoup,pyquery,pymysql,pymongo
# redis,flask(web库，代理),django,jupyter

# http://docs.jinkan.org/docs/flask/

# pip install beautifulsoup4

# w = urllib.request.urlopen("http://www.baidu.com")
# print(w)

# import selenium
# from selenium import webdriver
# driver = webdriver.Chrome() / # driver = webdriver.phantomjs()
#
# driver.get('http://www.baidu.com')
# driver.page_source

from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

doc = pq('<html>Hello</html>')
result = doc('html').text()

import pymysql
conn = pymysql.connect(host='localhost', user='root', password='123')


# import pymongo
# client = pymongo.MongoClient('localhost')
# db = client['newtestdb']
# db['table'].insert(('name': 'Bob'))
# db['table'].find_one(('name': 'Bob'))


# import redis
# r = redis.Redis('localhost', 6379)
# r.set('name', 'Bob')
# r.get('name')


