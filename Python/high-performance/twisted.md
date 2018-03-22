## twisted

### 安装
- 问题一
	
	```
	error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
	https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
	pip3 install C:\Users\Administrator\Downloads\Twisted-17.9.0-cp36-cp36m-win_amd64.whl
	pip3 install twisted
	```
- 问题二：
	
	```
	ModuleNotFoundError: No module named 'win32api'
	pip3 install pypiwin32
	```
- 问题三：
	- pip3 install pyopenssl

### twisted基本用法
```python
from twisted.web.client import getPage,defer
from twisted.internet import reactor

def all_done(arg):
    # print(arg)
    reactor.stop()

def callback(res):
    print(res)
    return 1

defer_list=[]
urls=[
    'http://www.baidu.com',
    'http://www.bing.com',
    'https://www.python.org',
]
for url in urls:
    obj=getPage(url.encode('utf=-8'),)
    obj.addCallback(callback)
    defer_list.append(obj)

defer.DeferredList(defer_list).addBoth(all_done)

reactor.run()
```

#### getPage详细用法
```python
from twisted.internet import reactor
from twisted.web.client import getPage
import urllib.parse


def one_done(arg):
    print(arg)
    reactor.stop()

post_data = urllib.parse.urlencode({'check_data': 'adf'})
post_data = bytes(post_data, encoding='utf8')
headers = {b'Content-Type': b'application/x-www-form-urlencoded'}
response = getPage(bytes('http://dig.chouti.com/login', encoding='utf8'),
                   method=bytes('POST', encoding='utf8'),
                   postdata=post_data,
                   cookies={},
                   headers=headers)
response.addBoth(one_done)

reactor.run()
``` 



