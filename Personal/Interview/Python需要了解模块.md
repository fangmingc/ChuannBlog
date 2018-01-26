## python需要了解模块 
之前我面试的时候，一般都会问一个问题：「能讲讲你日常开发中都用到了那些Python内置的模块吗」？我为啥爱问这么个问题呢：
1. 了解面试者日常的工作。

2. 了解面试者对技术的热情和主动性。

3. 侧面验证面试者技术水平。

非常遗憾的是，绝大多数的面试者的回答我都不满意。

那学会这些内置模块有多重要呢？ 我举五个例子吧：

1. 我做运维的时候，使用Python完成了一些打包和备份的脚本，也就是把某个目录压缩成各种格式（tar.gz、tar.bz2、zip）。 这个脚本其实打包压缩的部分还是比较复杂的。直到我看到了这个：

In : from shutil import make_archive
In : make_archive('archive_xxx', 'bztar')
Out: 'archive_xxx.tar.bz2'
有兴趣的可以翻一下源码。你想要的说不定标准库里面已经实现。当然，有标准库不满足的额外需求，也可以参照它实现。

2. 你可能接触过定时任务（crontab），它管理的任务很规矩，到点执行（当然精确度不那么高）。现在设想你有更复杂的任务需求：这个任务是动态的，也就是不一定啥时候就来排上队约定一个事件等着执行。这时候你可以想，这可以使用队列（Queue模块）啊，嗯也不错。难度再提高：加上优先级策略并能取消某个指定的已经放入队列的任务。现在思考下，这个怎么实现？其实很多工程实践的最好范例都在标准库中。sched模块中的scheduler类就是一个这样的通用的事件调度类。你可以学习它的实现。你问我它的实现多复杂？整个模块加上大幅的注释才134行。

3. 学习Python的过程中，一开始我对于装饰器contextmanager+yield怎么都不懂。直到我看了contextmanager的源代码, 其实非常简单就懂了。它的docstring清楚地不能再清楚了：

    Typical usage:                                                                               
                                                                                                 
        @contextmanager                                                                          
        def some_generator(<arguments>):                                                         
            <setup>                                                                              
            try:                                                                                 
                yield <value>                                                                    
            finally:                                                                             
                <cleanup>                                                                        
                                                                                                 
    This makes this:                                                                             
                                                                                                 
        with some_generator(<arguments>) as <variable>:                                          
            <body>                                                                               
                                                                                                 
    equivalent to this:                                                                          
                                                                                                 
        <setup>                                                                                  
        try:                                                                                     
            <variable> = <value>                                                                 
            <body>                                                                               
        finally:                                                                                 
            <cleanup>                                                                            
                           
4. 我之前使用多线程编程都这样用，在好长一段时间里面对于多进程和多线程之前怎么选择都搞得不清楚。看多了开源项目代码，我发现了好多人在用multiprocessing.dummy这个子模块，「dummy」这个词本身好奇怪，我决定去看多进程（multiprocessing）库的代码。「咦！怎么和多线程的接口一样呢」。后知后觉的我看到文档中这样说：

multiprocessing.dummy replicates the API of multiprocessing but is no more than a wrapper around the threading module.
恍然大悟！！！如果分不清任务是CPU密集型还是IO密集型，我就用如下2个方法分别试：

from multiprocessing import Pool
from multiprocessing.dummy import Pool
哪个速度快就用那个。从此以后我都尽量在写兼容的方式，这样在多线程/多进程之间切换非常方便。

5. 13-14年间，Flask还没怎么火，那时候装饰器风格的Web框架还有一个Bottle。我当时就直接想去看Bottle代码，发现一上来import了一堆模块，你先感受下bottle/bottle.py at master · bottlepy/bottle · GitHub ，第一感觉就是懵啊，这都是干什么的啊，为什么要用啊？这就是促使我去看标准库实现最重要的原因：学会了我才能更好的看懂别人写的代码。

但是不是所有的标准库都要一视同仁的看呢？你可以设置优先级，先看那些不可不知道的模块。我在这里列一下，并对它的用途和其中重要的类、函数的作用加以说明等。要是每个都写例子实在太多太密集，怕大家看不下去，我都用外部链接了。

1. argparse。 用来替代optparse的命令行解析库。如果你考虑用更直观的，推荐docopt，它使用docstring所见即所得实现命令行解析。
2. collections。 包含了一些额外的数据类型。其中的OrderedDict（有序列的字典）、defaultdict（带有默认值的字典）、namedtuple（通过创建带有字段属性的元组子类）和deque（高效实现插入和删除操作的双向列表）非常常用。
3. functools。 这个模块有一些非常有用的工具，其中的partial（偏函数）、wraps（将被包装函数的信息拷贝过来）、total_ordering（只需要定义2个__XX__方法就可实现对象对比的类装饰器）、cmp_to_key（将老式的比较函数转化为关键字函数）非常常用。
4. glob。 文件名的shell模式匹配，你不用遍历整个目录判断每个文件是不是符合，使用glob一句话就解决。
5. multiprocessing。多进程模块，这重要性就不说了。
6. os。应该是日常工作最常用的模块了，你是否了解它里面所有的函数和实现呢？举个例子，获取环境变量，我之前这样用：
In : os.environ.get('PYTHONPATH')
读完源码之后我学了一招：
os.getenv('PYTHONPATH')
好吧，省了5个字符。

7. Queue。这个模块用于多线程编程，它是一个线程安全的FIFO（先进先出）的队列实现。如果是多进程编程，选用multiprocessing.queues中的Queue、SimpleQueue、JoinableQueue这三个队列实现。 
8. SimpleHTTPServer。最简单地HTTP Server实现。不使用Web框架，一句：
python -m SimpleHTTPServer PORT
就可以运行起来静态服务。平时用它预览和下载文件太方便了。
9. subprocess。 如果你还被某些书籍引导使用os.system或者os.popen等模块，现在是放弃它们的时候了，这个模块会满足你绝大多数的系统命令执行、执行结果获取和解析等需求。其中最有用的是call（执行系统命令）、check_call（执行结果不为0则抛出异常）、check_output（最方便的获取执行的输出的函数）、Popen+PIPE（支持管道的多命令执行）。
10. threading。多线程模块，重要性也不必说。

当然啦，看的过程中还要多练习，也可以通过对应模块的测试代码了解模块。

无耻的广告：《Python Web开发实战》上市了！
欢迎关注本人的微信公众号获取更多Python相关的内容（也可以直接搜索「Python之美」）：