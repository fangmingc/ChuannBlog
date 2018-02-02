## flask-script
- 用于自定义命令行工具


### 安装和使用
- 安装
	- `pip3 install flask-script`
- 使用

	```python
	from flask_script import Manager, Server
	
	app = Flask(__name__)
	manager = Manager(app)
	
	# 创建启动服务的命令
	manager.add_command("runserver", Server())
	
	# 创建数据库迁移命令
	from flask_migrate import Migrate, MigrateCommand
	migrate = Migrate(app, db)
	manager.add_command('db', MigrateCommand)
	
	# 创建自定义命令
	@manager.option("-n", "--name", dest="name")
	@manager.option("-u", "--url", dest="url")
	def cmd(name, url):
	    print(name, url)
	```


