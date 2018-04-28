# git版本控制系统

## git 配置
- git log 展示的信息时中文乱码
	- `git config --global i18n.logoutputencoding utf-8`
- 配置用户名和邮箱
	- `git config user.name "username"`
	- `git config user.email 'usermail@163.com'`
- 配置ssh-key
	- 生成ssh-key：`ssh-keygen -t rsa -C "username@mail.cn" -b 4096`
		- 在之后的对话中输入密码
	- 查看ssh-key:`cat ~/.ssh/id_rsa.pub`
		- 复制key并保存在git设置中

## 操作命令
可以通过git 命令 --help调出官方文档查看相应命令文档

### git clone [.git文件]
- 克隆.git文件

### git add
- 添加版本追踪：git add [文件名]
- 追踪所有变化：git add .

### git commit
- 确认提交：git commit -m "提交说明"

### git pull
- 同步远端到本地:git pull

### git push
- 提交本地更改到远端:git push

### git reset
- 回退上一个版本：git reset --hard HEAD^  
- 回退指定版本：git reset --hard [版本号]

### git revert
- 删除最近一次提交：git revert HEAD

### git log
- 查看版本日志：git log

### git reflog
- 查看操作记录（仅限本地执行的操作）

### git stash
- 处理问题：
	- 新功能开发未完成，上一个版本出问题需要紧急修复
- 使用git stash将内容存到某个地方，工作区回到上一个版本的代码
	- 修复bug之后，使用git stash pop将暂存区的内容拿回来
		- 格外注意：
			- 修bug的代码可能会和stash缓存的工作代码冲突
	- git stash list
	- git stash clear
	- git stash pop
	- git stash apply
	- git stash drop
- 更多命令使用git stash --help查看

### git remote
- 远端仓库相关指令
- 先有本地文件，后有GitHub仓库，将本地文件上传至GitHub
	- git remote add origin fangmc@https://github.com/fangmingc/MyConponent.git
	- git push https://github.com/fangmingc/MyConponent.git

### git checkout
- 切换分支： git checkout [分支名]

### git merge
- 合并分支： git merge [分支名]

### git branch
- 查看所有分支
	- git branch --list
- 查看分支：git branch  
- 删除分支：git branch -d [分支名]
- 强制删除分支：git branch -D [分支名]


## 回退远端仓库
### 方法一
适用次数少的回退  
第一步：删除最后一次提交  
git revert HEAD  
第二步：提交更改
git push origin master   
### 方法二
慎重！慎重！慎重！  
务必在所有提交者都确认的情况使用本方法！！   
第一步：回退到指定版本  
git reset --hard HEAD[回退的版本号]   
第二步：强制提交更改   
git push origin master -f   


## git分支策略
[Git分支管理策略-阮一峰的网络日志](http://www.ruanyifeng.com/blog/2012/07/git.html)

### 主分支和开发分支
- 主分支master
	- 代码库应该有一个、且仅有一个主分支。所有提供给用户使用的正式版本，都在这个主分支上发布
	- Git主分支的名字，默认叫做master。它是自动建立的，版本库初始化以后，默认就是在主分支在进行开发。
- 开发分支Develop
	- 主分支只用来分布重大版本，日常开发应该在另一条分支上完成。我们把开发用的分支，叫做Develop。
	- 这个分支可以用来生成代码的最新隔夜版本（nightly）。如果想正式对外发布，就在Master分支上，对Develop分支进行"合并"（merge）。
		1. 创建master分支的develop分支：git checkout -b develop master
		2. 开发develop分支
		3. 切换到master分支：git checkout master
		4. 对develop分支进行合并：git merge --no-ff develop

	>--no-ff参数说明：
	>git默认执行快进式合并(fast-farward merge)，会将master分支指向develop分支的起始位置，这样不方便理解和管理
	>使用--no-ff表示执行正常的合并，即将develop分支和master分支合并后在master生成一次commit节点

### 临时性分支
用于应对一些特定目的的版本开发

- 功能（feature）分支
	- 为了开发某种特定功能，从Develop分支上面分出来的。开发完成后，要再并入Develop
	- feature-*的形式命名
	- 合并入develop后记得删除develop分支
		- git checkout -b feature-x develop
		- edit...
		- git checkout develop
		- git merge --no-ff feature-x
		- git branch -d feature-x

- 预发布（release）分支
	- 指发布正式版本之前（即合并到Master分支之前），我们可能需要有一个预发布的版本进行测试。
	- 预发布分支是从Develop分支上面分出来的，预发布结束以后，必须合并进Develop和Master分支。它的命名，可以采用release-*的形式。
		- git checkout -b release-1.2 develop
		- 确认没有问题后，合并到master分支
		- git checkout master
		- git merge --no-ff release-1.2
		- 对合并生成的新节点，做一个标签
		- git tag -a 1.2
		- 再合并到develop分支
		- git checkout develop
		- git merge --no-ff release-1.2
		- git branch -d release-1.2
- 修补bug（fixbug）分支
	- 软件正式发布以后，难免会出现bug。这时就需要创建一个分支，进行bug修补。
	- 修补bug分支是从Master分支上面分出来的。修补结束以后，再合并进Master和Develop分支。它的命名，可以采用fixbug-*的形式
	- 命令顺序类似预发布分支


## 项目上线
### 方式一
- 公司
	- 平时写代码
- gitlab
	- 各种项目版本，分支
- 公司服务器
	- 从gitlab下载master最新版本

### 方式二
- 公司
- gitlab
- 代码服务器
	- 编译代码/构建(Vue)
	- 分发代码到公司服务器
		- saltstack，远程推送文件，操纵服务器
- 公司服务器





