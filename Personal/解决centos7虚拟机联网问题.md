## 解决VMWare上centos7无法联网
- 适用情况：使用NAT模式联网
	- 桥接模式死活用不上，遂采用NAT模式，折腾了一整天才解决
- 以下条件都需要确认排查
	- windows防火墙关闭
	- 虚拟机防火墙关闭
	- VMWare网络编辑器：VMnet8，如
		- 子网Ip与主机局域网的地址不在同一网段
			- 子网IP:192.168.xx.0
			- 子网掩码：255.255.255.0
		- NAT设置中的网关设置为192.168.xx.2
	- 检查网卡设置，eg：网卡名ens33
		- /etc/sysconfig/network-scripts/ifcfg-ens33
			
			```conf
			TYPE=Ethernet
			PROXY_METHOD=none
			BROWSER_ONLY=no
			BOOTPROTO=dhcp
			DEFROUTE=yes
			IPV4_FAILURE_FATAL=no
			IPV6INIT=yes
			IPV6_AUTOCONF=yes
			IPV6_DEFROUTE=yes
			IPV6_FAILURE_FATAL=no
			IPV6_ADDR_GEN_MODE=stable-privacy
			NAME=ens33
			UUID=7b137af7-5b29-4766-99a7-1118af684915
			DEVICE=ens33
			ONBOOT=yes
			HWADDR=00:0c:29:67:5f:f0
			```	
		- MAC地址为通过ifconfig查询到的
			- 如无此命令则为表示系统为极简版，恕在下无能为力
	- 修改了设置记得重启网卡或者重启虚拟机
		- 重启网卡 /etc/init.d/network restart
		- 重启虚拟机 reboot




