## linux安装python3

1. 下载
	- `wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz` 
2. 解压
	- `tar zxvf Python-3.6.4.tgz`  
3. 编译
	- `cd Python-3.6.4`
	- `./configure —prefix=/etc/python/python3.6` 
	- `yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel`
		- 确保pip的时候不会有出错
	- `make && make install`
4. 启动
	- `python3`
	- 检查`pip3 --version`

5. 设置
	- `ln -s /etc/python/python3.6/bin/python3.6 /usr/bin/python3`
	- `ln -s /etc/python/python3.6/bin/pip3.6 /usr/bin/pip3`



