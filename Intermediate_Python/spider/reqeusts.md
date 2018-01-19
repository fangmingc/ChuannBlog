## reqeusts
```python
pip install requests
```
### 简单使用：百度关键字搜索
```python
import requests

# 百度搜索：https://www.baidu.com/s?wd=三体
# 请求方式：GET
# 请求头：
#       User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
# 请求体:
#       params={}

search_condition = input("请输入搜索条件：")

response = requests.get(
    url="https://www.baidu.com/s",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    },
    params={
        "wd": search_condition
    }
)

with open("ss.html", "w", encoding="UTF-8") as wf:
    wf.write(response.text)
```

### 请求与响应
#### 基于GET请求
- url
	- URL字符串
- params
	- 字典
	- GET请求所带的参数
- headers
	- 字典
	- 请求头数据
- cookies
	- 字典
	- 请求发送的cookie
- allow_redirects
	- 布尔值
	- 当有重定向时，是否重定向

##### 高级参数
- verify
	- 布尔值
	- 是否启用SSL证书认证，但是会有警告信息
	- from requests.package import urllib3
	- urllib3.disable_warnings()
	- 禁用警告信息
- proxies
	- 字典
	- IP代理，{'http': 'http://IP:port'}
- timeout
	- 浮点数
	- 超时时间，发出请求等待响应的时间，超过时间则抛出异常
- auth
	- 字典或HTTPBasicAuth实例
	- 用于访问需要认证才可以获取内容的页面
- files
	- 文件句柄
	- 上传文件

#### 基于POST请求
- 其他与Get请求一致
- data
	- 字典
	- post提交的数据

#### 响应
- 无论是get或是post请求，都会有response，都是Response类的对象
	- status_code
		- 数字
		- 响应状态码
	- headers
		- CaseInsensitiveDict的实例
		- 响应头信息
	- content
		- 字符串
		- bytes类型的响应内容
		- iter_content(),二进制迭代器，可以一行行读取响应
	- text
		- 字符串
		- unicode类型的响应内容
	- history
		- 列表
		- 保存重定向到在本响应之前的响应(都是对象)
	- cookies
		- RequestsCookieJar的实例，具有类似字典的结构
		- 保存响应接收的cookies
	- encoding
		- 设置响应内容的编码格式，默认ISO-8859-1
	- json
		- 直接获取json格式数据

### 综合练习1：自动登录GitHub
```python
import re
import requests

# 1. 第一步，获取登录页面
# 请求URL：http://github.com/login
# 请求方式：GET
# 请求头：
#       User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
# 请求体：
#       无

url1 = "http://github.com/login"
first_response = requests.get(
    url1,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    })
cookies_for_auth = first_response.cookies.get_dict()
authenticity_token = re.findall('name="authenticity_token".*?value="(.*?)"', first_response.text, re.S)[0]

# print(cookies_for_auth)
# print(authenticity_token)

# 2. 第二步，提交登陆数据
# 请求URL: https://github.com/session
# 请求方式：POST
# 请求头：
#   headers: {
#       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
#       "cookies": {....}
#       "Referer": "https://github.com/"
# }
#
# 请求体：
#   FormData: {
#       "commit":"Sign in"
#       "utf8":"✓"
#       "authenticity_token":"C5K8hW8DEwM5R9mFcXiN1ZZYhtFQMeKsq5pv0zdKPaxBC3H3SRIEBUiDrgYZ9bIOd9Gn7K2IpJCTOjGR/G+UUA=="
#       "login":"dsfdfasa"
#       "password":"adsfadsf"
#   }
url2 = "https://github.com/session"
username = "fangming99@outlook.com"

password = "无密码"                            # 未填密码

second_response = requests.post(
    url2,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Referer": "https://github.com/"
    },
    cookies=cookies_for_auth,
    data={
        "commit": "Sign in",
        "utf8": "✓",
        "authenticity_token": authenticity_token,
        "login": username,
        "password": password,
    },
    # allow_redirects=False
)
auth_cookie = second_response.cookies.get_dict()
print(second_response.status_code)


# https://github.com/settings/emails
url3 = "https://github.com/settings/emails"
third_response = requests.get(
    url3,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Referer": "https://github.com/"
    },
    cookies=auth_cookie,
)
# 检测是否登录成功
print("fangming99@outlook.com" in third_response.text)
for history in third_response.history:
    print(history, type(history))
```

### 综合练习2：自动登录拉勾网投递简历
- 已失效

