## flask信号
- 信号的作用
	- 降低代码的耦合度
		- eg:特殊情况发邮件/短信等
	- 在请求开始到结束之间自定义一些无返回值的操作

### blinker
- pip3 install blinker

#### flask内置十个信号
- 主流程
 	1. appcontext_pushed = _signals.signal('appcontext-pushed')            # app上下文push时执行
	2. request_started = _signals.signal('request-started')                # 请求到来前执行
	3. request_finished = _signals.signal('request-finished')              # 请求结束后执行
	4. request_tearing_down = _signals.signal('request-tearing-down')      # 请求执行完毕后自动执行（无论成功与否）
	5. appcontext_tearing_down = _signals.signal('appcontext-tearing-down')# 请求上下文执行完毕后自动执行（无论成功与否）
	6. appcontext_popped = _signals.signal('appcontext-popped')            # app上下文pop时执行
- 模板相关	
	- 2.1 before_render_template = _signals.signal('before-render-template')  # 模板渲染前执行
	- 2.2 template_rendered = _signals.signal('template-rendered')            # 模板渲染后执行
- 异常相关
	- 2/3 got_request_exception = _signals.signal('got-request-exception')    # 请求执行出现异常时执行
- 闪现相关
	- message_flashed = _signals.signal('message-flashed')                # 调用flask在其中添加数据时，自动触发

#### flask自定义信号
```python
from flask.singals import _singals

test = _singals.singal("test")


def func(*args, **kwargs):
    print(args, kwargs)


test.connect(func)
```
- 在视图函数中使用`test.send(...)`用于触发信号

### 信号与特殊装饰器的区别
- 信号不需要返回值，特殊的装饰器视情况而定
- 信号何用？
	- 自定义的一些操作
