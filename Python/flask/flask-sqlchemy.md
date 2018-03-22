## flask-sqlchemy
- SQLAlchemy在Flask上的适应版本


### 安装和使用
- 安装
	- `pip3 install flask-sqlalchemy`
- 初始化

	```python
	from flask_sqlalchemy import SQLAlchemy
	
	app = Flask(__name__)
	db = SQLAlchemy(app)
	```

- 使用
	- db.session.query()
	- 参考SQLAlchemy的使用





