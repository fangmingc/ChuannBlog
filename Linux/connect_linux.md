## 常见问题
1. Xshell无法远程连接服务器(屌丝去洗浴中心)
	- 道路是否通畅
		- 主机ping虚拟机
			- ping不同
				- 请求超时
				- 无法访问目标主机
		- 原因检查
			1. 检查服务器是否有ip，网卡是否启动
			2. 检查vmware的虚拟网络编辑器中的子网ip和子网掩码是否正确
			3. 保证vmware相关的服务是否正常运行
				- win+r  services.msc  
				- 检查VMware Authorization Service是否启动
				- 检查VMware NAT Service是否启动
				- 检查VMware DHCP Service是否启动
			4. 网络连接
				- 任意打开文件夹，在地址栏输入`网络连接`，回车
				- 检查VMware Virtual Ethernet Adapter for VMnet1是否启动
				- 检查VMware Virtual Ethernet Adapter for VMnet8是否启动
	- 是否有劫财劫色
		- Iptables
		- Selinux
	- 洗浴中心是否提供你想要的服务

- 端口
	- 22----远程连接服务 sshd
		- 测试22端口，`telnet 10.0.0.200 22`
			- telnet 命令找不到----使用Xshell的本地shell即可，cmd默认未安装telnet

			```
			Connecting to 10.0.0.200:22...
			Connection established.
			To escape to local shell, press 'Ctrl+Alt+]'.
			SSH-2.0-OpenSSH_5.3
			```
2. linux无法上网
	- 确认是否能上网
		- `ping www.baidu.com`
	- 确认是否是DNS问题
		- 直接ping一下外网ip，如果成功说明是DNS问题
			- DNS服务器的
				- `ping 223.5.5.5`
				- `ping 114.114.114.114`
			- `ping 111.13.100.91`，百度
		- 确认是DNS问题后
			- 编辑网卡，`vim /etc/sysconfig/network-scripts/ifcfg-eth0`
			- 重启网卡，`/etc/init.d/network restart`
	- 确认是否是网卡配置问题
	- 确认是否是vmware网关配置问题
	- 确认是否是windows网络连接问题
		- 本地连接>属性>共享>取消选择允许其他网络用户通过此计算机的Internet连接


