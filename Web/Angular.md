## Angular
- Angular 是一个开发平台。它能帮你更轻松的构建 Web 应用。Angular 集声明式模板、依赖注入、端到端工具和一些最佳实践于一身，为你解决开发方面的各种挑战。Angular 为开发者提升构建 Web、手机或桌面应用的能力。

### 快速上手
#### 设置开发环境
- 检查node和npm
	- `node -v` 和 `npm -v`
		- node必须大于8.x
		- npm必须大于5.x
	- 可能遇到的问题：
		- ubuntu系统下`apt install nodejs-legacy`，然后`node -v`查看版本仅4.2.6，版本过低
		- 卸载之前的node后按照以下以流程重新安装
			- 安装nodejs
				- `apt install nodejs`
				- `apt install nodejs-legacy`
				- `apt install npm`
			- 更新npm镜像源
				- `npm config set registry https://registry.npm.taobao.org`
				- `npm config list`
			- 安装n管理器(npm下的nodejs版本管理模块)
				- `npm install -g n`
			- 更新nodejs
				- `n lastest`下载最新版本
				- `n stable`下载稳定版本
				- 输入`n`通过上下键选择版本，回车键确认(使用ssh工具可能会导致显示不及时，建议新开窗口查看)
			- `node -v`查看是否更新了版本
- 安装angular cli(命令行工具)
	- `npm install -g @angular/cli`


#### 创建新项目
- `ng new my-app`
- Angular CLI 会安装必要的 NPM 包、创建项目文件，并在该项目中生成一个简单的默认应用。这可能要花一点时间。
	- 你可以使用 ng add 命令往新项目中添加一些预先打包好的功能。 ng add 命令会通过应用来自特定 NPM 包中的图纸（schematic）来转换此项目。 要了解更多，参见 Angular CLI 文档。
	- 比如 Angular Material 就为一些典型布局提供了图纸。参见 Angular Material 文档。

#### 启动服务器
- 进入项目
	- `cd my-app`
- 启动项目
	- `ng server --help`获取启动项目的参数说明
	- `ng serve  --host 0.0.0.0 --port 4200 --open`启动服务并接受来自所有ip的请求，监听4200端口，不添加--host和--prot参数默认监听127.0.0.1:4200
- 此时访问ip:4200则可以看到angluar的欢迎页

#### 编辑你的第一个Angluar组件
-  CLI 为你创建了第一个 Angular 组件。 它就是名叫 app-root 的根组件。 你可以在 ./src/app/app.component.ts 目录下找到它。
	-  修改title可以修改页面上欢迎语中的字符
-  打开 src/app/app.component.css 并给这个组件设置一些样式
	
	```css
	h1 {
	  color: #369;
	  font-family: Arial, Helvetica, sans-serif;
	  font-size: 250%;
	}
	```


 


