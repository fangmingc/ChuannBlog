## asyncio
- 可以检测io操作，在不同任务之间切换

### 基本使用
```python
import asyncio


@asyncio.coroutine
def task(task_id, senconds):
    print('%s is start' % task_id)
    yield from asyncio.sleep(senconds)  
	# 只能是网络IO，检测到IO后切换到其他任务执行
	# 这里用的是自带的sleep方法，可以被检测，但无实际意义
    print('%s is end' % task_id)


tasks = [task(task_id="任务1", senconds=3), task("任务2", 2), task(task_id="任务3", senconds=1)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

### 实现http协议
```python
import asyncio
import uuid

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'


def parse_page(host, res):
    print('%s 解析结果 %s' % (host, len(res)))
    with open('%s.html' % (uuid.uuid1()), 'wb') as f:
        f.write(res)


@asyncio.coroutine
def get_page(host, port=80, url='/', callback=parse_page, ssl=False):
    # 步骤一（IO阻塞）：发起tcp链接，是阻塞操作，因此需要yield from
    if ssl:
        port = 443
    print('下载 http://%s:%s%s' % (host, port, url))

    print("=======", "与%s建立tcp连接" % host)
    recv, send = yield from asyncio.open_connection(host=host, port=443, ssl=ssl)

    # 步骤二：封装http协议的报头，因为asyncio模块只能封装并发送tcp包，因此这一步需要我们自己封装http协议的包
    request_headers = """GET %s HTTP/1.0\r\nHost: %s\r\nUser-agent: %s\r\n\r\n""" % (url, host, user_agent)
    # requset_headers="""POST %s HTTP/1.0\r\nHost: %s\r\n\r\nname=egon&password=123""" % (url, host,)
    request_headers = request_headers.encode('utf-8')

    # 步骤三（IO阻塞）：发送http请求包
    send.write(request_headers)
    print("=======", "向%s发送http请求" % host)
    yield from send.drain()

    # 步骤四（IO阻塞）：接收响应头
    print("=======", "接受来自%s的响应头" % host)
    while True:
        line = yield from recv.readline()
        if line == b'\r\n':
            break
        # print('%s Response headers：%s' % (host, line))

    # 步骤五（IO阻塞）：接收响应体
    print("=======", "接受来自%s的响应体" % host)
    text = yield from recv.read()

    # 步骤六：执行回调函数
    callback(host, text)

    # 步骤七：关闭套接字
    send.close()  # 没有recv.close()方法，因为是四次挥手断链接，双向链接的两端，一端发完数据后执行send.close()另外一端就被动地断开


if __name__ == '__main__':
    tasks = [
        # 每个都是生成器
        get_page('www.baidu.com', url='/s?wd=美女', ssl=True),
        get_page('www.amazon.com', url='/', ssl=True),
    ]

    # 事件循环
    loop = asyncio.get_event_loop()
    # asyncio启动任务并监测任务执行情况
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
```
