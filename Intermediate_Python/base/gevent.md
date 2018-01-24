## gevent
- 基于grennlet实现的协程

- monkey
	- patch_all()
		- 给python中的有IO阻塞的模块打补丁，让阻塞可以被gevent识别
		- eg:time.sleep()就不能被gevent识别，打上补丁后就可以

- pool
	- 协程池

### 使用
- 简单示例

	```python
	# 创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的
	g1 = gevent.spawn(func, 1, 2, 3, x=4, y=5)
	
	g2 = gevent.spawn(func2)
	
	g1.join() # 等待g1结束
	
	g2.join() # 等待g2结束
	
	# 或者上述两步合作一步：gevent.joinall([g1,g2])
	
	g1.value	# 拿到func1的返回值
	```
- 遇到IO阻塞时会自动切换任务

	```python
	import gevent
	def eat(name):
	    print('%s eat 1' %name)
	    gevent.sleep(2)
	    print('%s eat 2' %name)
	
	def play(name):
	    print('%s play 1' %name)
	    gevent.sleep(1)
	    print('%s play 2' %name)
	
	
	g1=gevent.spawn(eat,'egon')
	g2=gevent.spawn(play,name='egon')
	g1.join()
	g2.join()
	#或者gevent.joinall([g1,g2])
	print('主')
	```

### gevent实现爬虫

```python
from gevent import monkey;monkey.patch_all()
import gevent
import requests

def get_page(url):
    print('GET:%s' %url)
    response=requests.get(url)
    print(url,len(response.text))
    return 1

# g1=gevent.spawn(get_page,'https://www.python.org/doc')
# g2=gevent.spawn(get_page,'https://www.cnblogs.com/linhaifeng')
# g3=gevent.spawn(get_page,'https://www.openstack.org')
# gevent.joinall([g1,g2,g3,])
# print(g1.value,g2.value,g3.value) #拿到返回值


#协程池
from gevent.pool import Pool
pool=Pool(2)
g1=pool.spawn(get_page,'https://www.python.org/doc')
g2=pool.spawn(get_page,'https://www.cnblogs.com/linhaifeng')
g3=pool.spawn(get_page,'https://www.openstack.org')
gevent.joinall([g1,g2,g3,])
print(g1.value,g2.value,g3.value) #拿到返回值
```
