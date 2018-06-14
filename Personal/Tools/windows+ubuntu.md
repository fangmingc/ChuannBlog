## Windows用ubuntu子系统开发
1. 打开开发者模式
	- 设置->更新和安全->针对开发人员->开发人员调试
	- <img src="http://chuann.cc/Personal/Tools/img/settings.png">


2. 启用linux子系统组件
	- 控制面板->程序->程序和功能->启用或关闭windos功能->适用于Linux的windows子系统
	- <img src="http://chuann.cc/Personal/Tools/img/binsubsystem.png">

3. 下载安装
	- 应用商店->搜索Ubuntu->选择喜欢的版本->获取

4. 使用准备
	- 用户
		- 创建新用户
			- 第一次启动ubuntu会创建一个非root用户，也是ssh登陆的用户
			- 因暂无法确定的原因，ssh连子系统的时候不能使用root用户
		- 设置root用户密码
			- `passwd`然后就可以修改UNIX密码即root密码
	- 启用ssh服务
		- 生成公钥
			- 根据缺少的信息安装
		- 配置ssh
			- `vim /etc/ssh//sshd_config`
			- 设置`Port 22`为`Prot 23`
			- 设置`PasswordAuthentication no` 为`PasswordAuthentication yes`
	- 编写快捷启动脚本
		- 安装expect: `sudo apt install expect`
		- 启动ssh:bin_ssh.sh
			- `cd /home/你的用户名/`
			- `vim bin_ssh.sh`
	
				```bash
				#!/usr/bin/expect
				spawn sudo service ssh start
				expect {
				  "*pass*" {send "chuanguang\r"}
				}
				interact
				```
			- `chmod +x bin_ssh.sh`
		- 切换工作路径：start.sh
			- `cd /home/你的用户名/`
			- `vim start.sh`
	
				```bash
				#!/usr/bin/expect
				
				cd /mnt/c/company	#切换到你的工作目录
				spawn su root		#切换到root用户
				expect {
				  "*assw*" {send "password\r"} #自动登陆
				}
				expect {
				  "*@DESK*" {send "source /mnt/c/company/venv/for_actuary/bin/activate\r"} # 启用虚拟环境
				}
				interact  # 保留交互界面
				```
			- `chmod +x start.sh`
5. 开始使用
	- 启动子系统
	- 执行`./bin_ssh.sh`
	- 打开x-shell链接子系统，执行`./start.sh`
6. 常见问题：
	- 子系统没有IP?
		- 安装任意虚拟机模拟软件(vmware、virtualbox等)安装虚拟网卡
	- ssh连接失败？
		- 检查ssh服务是否启动成功？
		- 启动时有任何报错/警告信息？
		- 检测是否配置正确
	- linux包无法使用？
		- 子系统具有局限性，无法完全支持linux功能
	- ubuntu根目录在哪？
		- `C:\Users\windows下你的用户名\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs`
		- **注意**不要随意修改这里的文件！容易导致无法修复的bug
	- 无法安装部分命令？
		- 修改apt源


