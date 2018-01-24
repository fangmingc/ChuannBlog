## aiohttp
- 用asyncio定义http协议还需要手动，使用本模块则免除这一步骤

### 整合asyncio的模拟http请求
```python
import asyncio

import aiohttp


@asyncio.coroutine
def get_page(url):
    print('GET:%s' % url)
    response = yield from aiohttp.request('GET', url)

    data = yield from response.read()

    print("解析", url, len(data.decode("utf-8")))
    response.close()
    return len(data.decode("utf-8"))


tasks = [
    get_page('https://www.python.org/doc'),
    get_page('https://www.cnblogs.com/linhaifeng'),
    get_page('https://www.openstack.org')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

print('=====>', results)  # [1, 1, 1]

```

