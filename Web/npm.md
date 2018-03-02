## npm
- NPM是随同NodeJS一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：
	- 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
	- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
	- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

### 介绍与安装
- 新版的nodejs已经集成了npm，所以安装Node.js后，npm也一并安装好了。
- 可以通过输入 "npm -v" 来测试是否成功安装，出现版本提示表示安装成功

- 升级npm
	- `npm install npm -g`
	- `sudo npm install npm -g`

### 使用
- 帮助
	- `npm help`可查看所有帮助
	- `npm help <command>`可查看某条命令的详细帮助，如`npm help install`
- 安装模块
	- 安装指定模块`npm install <Module Name>`
	- 安装好之后，express 包就放在了工程目录下的 node_modules 目录中，因此在代码中只需要通过 require('express') 的方式就好，无需指定第三方包路径。
		- `var express = require('express');`
	- 全局安装与本地安装
		- npm 的包安装分为本地安装（local）、全局安装（global）两种，从敲的命令行来看，差别只是有没有-g
	
			```npm
			npm install express          # 本地安装
			npm install express -g   # 全局安装
			```
		- 全局安装
			1. 将安装包放在 /usr/local 下或者你 node 的安装目录。
			2. 可以直接在命令行里使用。
		- 本地安装
			1. 将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
			2. 可以通过 require() 来引入本地安装的包。
		- 如果你希望具备两者功能，则需要在两个地方安装它或使用 npm link
	- (项目目录下)根据package.json安装`npm install`
	- 参数
		- `npm install <Module Name> --save` 自动把模块和版本号添加到package.json的dependencies部分
		- `npm install <Module Name> --save-dev` 自动把模块和版本号添加到package.json的devdependencies部分
- 查看安装信息
	- `npm list/ls/la`
	- 查看所有全局安装的模块`npm list -g`
	- 查看某个模块的版本号`npm list grunt`
- package.json
	- 位于模块的目录下，用于定义包的属性
	- 属性说明
		- name 包名。
		- version  包的版本号。
		- description  包的描述。
		- homepage  包的官网 url 。
		- author  包的作者姓名。
		- contributors  包的其他贡献者姓名。
		- dependencies  依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。
		- repository  包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。
		- main  main 字段指定了程序的主入口文件，require('moduleName') 就会加载这个文件。这个字段的默认值是模块根目录下面的 index.js。
		- keywords  关键字
- 卸载模块
	- 我们可以使用以下命令来卸载 Node.js 模块。
		- `npm uninstall express`
	- 卸载后，你可以到 /node_modules/ 目录下查看包是否还存在，或者使用以下命令查看：
		- `npm ls`

