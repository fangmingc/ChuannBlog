## Django命令

### model相关
- 将models.py中定义的类编译：`python manage.py makemigrations`
- 执行编译文件：`python manage.py migrate`
- 清空数据库：`python manage.py flush`
- 回退数据库迁移
	- `python manage.py migrate app_name 0010_previous_migreation`
	- 可以删除migrations文件，0011_migration_to_revert.py
	- 重新生成migrations文件
- 回退app所有migrations
	- `python manage.py migrate app_name zero`
- 查看migrations文件
	- `python manage.py showmigrations app_name`

### 导出/导入数据
- 导出所有数据：`python manage.py dumpdata > db.json`
- 导出某个app:`python manage.py dumpdata app_name > app_name.json`
- 导出某个表:`python manage.py dumpdata app_name.table_name > app_name.table_name.json`
- 不要某个库或表：`python manage.py dumpdata --exclude app_name/app_name.table_name > db.json`
- 美化显示：`python manage.py dumpdata --indent 2 > db.json`
- 指定格式：`python manage.py dumpdata --indent 2 --format xml > db.xml`
	- 可选json，xml，yaml

- 导入数据
	- `python manage.py loaddate db.json`

### i18n&l10n
- `python manage.py compilemessages`

