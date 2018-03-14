## linux必知必会

### 虚拟机使用须知
- 刚装好时做好快照
	- 秘诀：挂起虚拟机后快照速度极快


### 命令使用相关
- 命令行
	- `[root@localhost ~]#`  [用户名@主机名 ~]#
	- 命令格式
		- 命令+空格+参数1+空格+参数2
		- `rm -f /tmp`

- linux的目录结构
	- 一切从根目录`/`开始

- 快捷键
	- tab键 自动补全命令或目录
	- ctrl+L 清屏   clear命令
	- ctrl+c 终止当前操作

- 相对路径、绝对路径
	- 绝对路径，从根开始的路径，如/data
	- 相对路径，不是从根开始的路径，相对于当前路径，如data

- 管道
	- 符号`|`
	- 把前面命令的结果，通过管道传递给后面的命令


### 常用命令
1. 获取帮助
	- help [命令]
	- man [命令]
2. 创建目录，mkdir
	- 参数
		- 创建多层目录，`mkdir -p /old/data/test`
3. 显示当前目录文件，ls
	- 参数
		- l，查看详细
		- a，查看所有文件
		- h，人性化展示
4. 切换目录，cd
5. 查看当前位置，pwd
6. 创建文件，touch
7. 编辑文件，vim或vi
	- 进入编辑模式，i
	- 退出编辑模式，Esc键
	- 保存退出
		- 输入`:wq`
	- 强制退出，不保存
		- `:q!`
	- 复制当前行，yy
	- 粘贴，p
	- 剪切，dd
	- 撤销，u
	- 恢复，ctrl+r
	- 显示行号，`set nu`
8. 查看文件内容，cat
	- 显示文件内容的行号
		- `cat -n 文件名`
9. 输出字符串，echo
	- 输出到屏幕，`echo "字符串"`
	- 追加输出重定向--追加内容到文件，`echo "oldboy.edu.com" >> /data/oldboy.txt`
	- 重定向，清空文件内容，写入字符串内容，`echo "oldboy.com" > /data/oldboy.txt`
10. 拷贝/复制文件，cp
	- 复制文件到指定目录，`cp 原文件 目的目录`
	- 备份，`cp 原文件 原文件.bak`
11. 移动，mv
	- 移动文件到指定目录，`mv 原文件 目的目录`
	- 重命名，`cp 原文件 新文件`
12. 删除文件，rm
	- `rm 文件`
	- 参数
		- r，删除目录
		- f，强制删除，不需确认
13. 查找文件，find
	- 寻找文件，`find 寻找目录范围 -type f -name "文件名"`
		- `find / -type f -name "oldboy.txt"`
		- 通配符，`find /data -type f -name "*.txt"`
		- 参数
			- 计算文件大小，size，`+1M`表示大于1Mb，`-1K`表示小于1Kb
	- 寻找目录，`find 寻找目录范围 -type f -name "目录名"`
		- `find / -type d -name "data"`
	- 管道使用
		- find与xargs配合
		- `find /root/ -type d -name "*.log" |xargs ls -l`
14. 显示指定行号的内容，
	- 创建文件`seq 40 > ett.txt`
	- `awk 'NR==20' test.txt`
	- `awk 'NR>=20 && NR<=30' ett.txt`
	- `awk 'NR<5 || NR>35' ett.txt`
15. 替换
	- 准备数据

		```linux
		mkdir -p /oldboy/test
		cd /oldboy
		echo "oldboy">test/del.sh
		echo "oldboy">test.sh
		echo "oldboy">t.sh
		touch oldboy.txt
		touch alex.txt
		```
	- 将每一个字母替换为'SO'，`sed 's#[a-zA-A]#SO#g' t.sh`
	- 将每一个字母替换为'oldgirl'，且备份文件存于'原文件名.bak'，`sed -i.bak 's#[a-zA-A]#oldgirl#g' t.sh`
	- 替换多个文件中的内容
		- 检测是否有错，`find /oldboy/ -type f -name "*.sh" |xargs sed 's#oldboy#newgirl#g'`
		- 正式执行，`find /oldboy/ -type f -name "*.sh" |xargs sed -i 's#oldboy#newgirl#g'`
		- 检查结果，`find /oldboy/ -type f -name "*.sh" |xargs cat`
16. 备份多个文件，打包压缩备份
	- tar，打包压缩
		- 打包压缩，`tar zcf /tmp/etc.tar.gz /etc/`
			- z，gzip软件进行压缩
			- c，打包，创建包
			- v，显示过程
			- f，file，指定压缩包
		- 查看压缩包
			- `tar tf etc.tar.gz`
		- 解压
			- `tar xf etc.tar.gz`
17. 安装软件
	- yum 替人解决依赖关系
	- rpm包 需要自己解决依赖关系
	- 编译安装 
		- `./congigure`，可以在这里配置各种参数
		- `make`
		- `make install`
 


