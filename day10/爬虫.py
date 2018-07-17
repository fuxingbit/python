# @Time    : 2018/7/17 9:58
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

from gevent import monkey
import gevent, time
from urllib.request import urlopen

monkey.patch_all() # 把当前程序的所有IO操作单独做标记, 不写这个，urllib默认同步


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    # f = open("url.html", "wb")
    # f.write(data)
    # f.close()
    print('%d bytes received from %s.' % (len(data), url))


urls = ['https://www.python.org/',
        'https://www.baidu.com/',
        'https://github.com/',
        ]

start_time = time.time()
for i in urls:
    f(i)
print("同步cost：", time.time() - start_time)

async_start_time = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost：", time.time() - async_start_time)
