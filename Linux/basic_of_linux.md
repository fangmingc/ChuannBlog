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
	- ctrl+d 退出当前用户
	- esc+. 使用上一个命令的最后一个参数

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
	- 显示行号，`:set nu`
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
		- `yum install  tree  telnet -y`
	- rpm包 需要自己解决依赖关系
		- 检查命令是否安装，只能查询yum、rpm包安装的
			- `rpm -qa tree`
			- `rpm -qa tree telnet lrzsz`
		- 检查软件包的内容
			- `rpm -ql 命令名`
		- 安装
			- `rpm -ivh rpm包路径`
	- 编译安装 
		- `./congigure`，可以在这里配置各种参数
		- `make`
		- `make install`
18. 挂载光盘
	- 把光盘放入光驱
		- 通过VMWare管理虚拟机，在光驱选项选中linux-iso文件
	- 挂载光盘
		- linux下光盘位置，`ls -l /dev/cdrom`
		- 挂载：给光盘腾个位置
			- `mount /dev/cdrom /mnt/`
		- `cd /mnt/`
		- `rpm -ivh /mnt/Packages/telnet-0.17-48.el6.x86_64.rpm`
19. 显示相关
	- 查看磁盘使用情况，`df -h`
	- 查看文件前10行
		- `head /etc/passwd`
		- `head -5 /etc/passwd`，前五行
	- 查看文件后10行
		- `tail /etc/passwd`
		- `tail -5 /etc/passwd`，后五行
20. yum源
	- 安装的命令不在三大基本仓库

		```linux
		[root@chuan ~]# yum install sl cowsay -y
		Loaded plugins: fastestmirror, security
		Setting up Install Process
		Loading mirror speeds from cached hostfile
		 * base: mirrors.aliyun.com
		 * extras: mirrors.163.com
		 * updates: mirrors.nwsuaf.edu.cn
		No package sl available.
		No package cowsay available.
		Error: Nothing to do
		```
	- 增加epel源，extra package for enterprise linux，Fedora制作的
		- `yum install epel-release -y`
	- 再次安装
		- `yum install sl cowsay -y`
	- 使用
		- `sl`
		- `cowsay "hello world"`
21. 关闭iptables和selinux
	- 临时关闭防火墙
		- 执行两次，`/etc/init.d/iptables stop`
	- 永久关闭防火墙
		- 关闭开机自启动
			- 查看开机自启动服务，`chkconfig`
			- 检查防火墙自启动服务，`chkconfig |grep iptables`
			- 关闭，`chkconfig iptables off`
22. 运行级别
	- 0，关机状态
	- 1，单用户模式，可以用来重新重置root用户密码
	- 2，多用户模式，但是没有NFS软件(做存储)
	- 3，完全的多用户模式，命令行、文本模式
	- 4，尚未被使用的
	- 5，X11，桌面、图形界面模式
	- 6，重启状态
	- 查询当前系统运行级别
		- `runlevel`
	- 临时+永久修改运行模式
		- 修改`/etc/inittab`文件最后
		- `tail -1 /etc/inittab`
23. 用户操作
	- 查看版本
		- 系统版本，`cat /etc/redhat-release `
		- 内核版本，`uname -r`
	- 增加用户
		- `useradd oldboy`
	- 查看用户信息
		- `id oldboy`
		- root用户uid为0
	- 设置密码
		- `passwd oldboy`
	- 切换用户
		- `su - oldboy`
	- 我是谁？
		- `whoami`
24. 如何进入单用户模式
	- 重启
		- 推荐使用shutdown
			- 10分钟后重启，会给所有用户通知10分钟后重启`shutdown -r 10`
	- 在加载系统时，快速摁任意键终止启动系统，按a或e
		- 按a
			- 添加空格和数字1或single然后回车就可以进入单用户模式
		- 按e
			- 上下选择linux内核，按e编辑
			- 添加空格和数字1然后回车
			- 回到选择框，按b进入单用户模式
25. 如何进入救援模式
	- 插入光盘
	- `resuce installed system`
26. selinux
	- NSA弄出来限制root用户的，工作中通常关闭
	- `ll /etc/selinux/config`
		- 永久修改，将配置文件的第7行修改为disabled
			- 使用替换修改
				- `sed 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config`
				- 确认无误后正式修改`sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config`
			- 编辑修改，`vim /etc/selinux/config`
		- 临时修改
			- 查看你当前selinux状态，`getenforce`
			- 修改状态selinux状态，`setenforce 0`
27. 定时任务，crontab [-l(list)] [-e(edit)]
	- 定时任务格式
		- `分钟 小时 日期 月份 周几 执行命令`
		- 特殊符号
			- `*`表示每次，`* * * * *`表示每天每时每分执行一次
			- `*/n`，表示每隔n(分钟/小时/天)执行
	- 例子
		- 每分钟向/tmp/oldboy.txt追加名字
			- 编辑定时任务，`crontab -e`
			- 写入定时任务，`* * * * * echo chuck >> /tmp/oldboy.txt`
			- 实时更新，`tail -f /tmp/oldboy.txt`
		- 每三分钟同步一次系统时间
			- 检查命令是否可以正常运行，`/usr/sbin/ntpdate ntp1.aliyun.com`
			- 修改当前时间，`date -s "20100101"`
			- 编辑定时任务，`crontab -e`
			- 写入定时任务，`*/3 * * * * /usr/sbin/ntpdate ntp1.aliyun.com`
			- 检查是否成功，`date`，`tail /var/log/cron`
	- 查看定时任务日志
		- `ls -l /var/log/cron`
		- 日志格式
			- `(root) CMD (echo chuck >> /tmp/oldboy.txt)`
			- (执行用户) 命令格式 (执行命令)
	- 常见错误
		- `You have mail in /var/spool/mail/root`
			- 需要将定时任务的结果定向到空或追加到文件
			- 定向到空，`*/3 * * * * /usr/sbin/ntpdate ntp1.aliyun.com > /dev/null 2>&1`
			- 追加到文件，`*/3 * * * * /usr/sbin/ntpdate ntp1.aliyun.com > /dev/cron.log 2>&1`
28. 时间
	- 查看时间
		- `date`
	- 修改时间
		- `date -s "20180101"`
	- 同步时间
		- `/usr/sbin/btpdate ntp1.aliyun.com`


