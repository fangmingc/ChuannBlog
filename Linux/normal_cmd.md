## 常用命令
1. 寻找指定程序并杀掉：`ps -ef |grep "uwsgi --ini" | awk '{print $2}'|xargs kill -9`
2. 寻找指定目录下的指定文件后缀并删除：`find /root/chuan/ -name "*.pyc" | xargs rm -rf`

