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
				- `apt install nodejs-legacy`n
				- 
				- `apt install npm`
			- 更新npm镜像源
				- `npm config set registry https://registry.npm.taobao.org`
				- `npm config list`
			- 安装n管理器(npm下的nodejs版本管理模块)
				- `npm install -g n`
			- 更新nodejs
				- `n latest`下载最新版本
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
	- `ng serve  --host 0.0.0.0 --port 4200`启动服务并接受来自所有ip的请求，监听4200端口，不添加--host和--prot参数默认监听127.0.0.1:4200
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

#### 项目文件概览
- src文件夹
	- 应用代码位于 src 文件夹中
	- 所有的 Angular 组件、模板、样式、图片以及你的应用所需的任何东西都在那里。 
	- 这个文件夹之外的文件都是为构建应用提供支持用的。

<table>
<tbody><tr>
<th><p translation-result="">      文件</p><p translation-origin="off">      File</p></th> <th><p translation-result="">      用途</p><p translation-origin="off">      Purpose</p>
</th></tr><tr><td>
<p translation-origin="off">      <code>app/app.component.{ts,html,css,spec.ts}</code></p></td><td>
<p translation-result="">      使用 HTML 模板、CSS 样式和单元测试定义 <code>AppComponent</code> 组件。
它是<strong>根</strong>组件，随着应用的成长它会成为一棵组件树的根节点。</p><p translation-origin="off">      Defines the <code>AppComponent</code> along with an HTML template, CSS stylesheet, and a unit test.
It is the <strong>root</strong> component of what will become a tree of nested components
as the application evolves.</p>

    </td></tr><tr><td>
<p translation-origin="off">      <code>app/app.module.ts</code></p>
</td><td><p translation-result="">      定义 <code>AppModule</code>，<a href="https://www.angular.cn/guide/bootstrapping" title="AppModule: 根模块">根模块</a>为 Angular 描述如何组装应用。
目前，它只声明了 <code>AppComponent</code>。
不久，它将声明更多组件。</p><p translation-origin="off">      Defines <code>AppModule</code>, the <a href="https://www.angular.cn/guide/bootstrapping" title="AppModule: the root module">root module</a> that tells Angular how to assemble the application.
Right now it declares only the <code>AppComponent</code>.
Soon there will be more components to declare.</p>

</td></tr><tr><td>
<p translation-origin="off">      <code>assets/*</code></p></td><td><p translation-result="">      这个文件夹下你可以放图片等任何东西，在构建应用时，它们全都会拷贝到发布包中。</p><p translation-origin="off">      A folder where you can put images and anything else to be copied wholesale
when you build your application.</p>

</td></tr><tr><td><p translation-origin="off">      <code>environments/*</code></p></td><td>
<p translation-result="">      这个文件夹中包括为各个目标环境准备的文件，它们导出了一些应用中要用到的配置变量。
这些文件会在构建应用时被替换。
比如你可能在生产环境中使用不同的 API 端点地址，或使用不同的统计 Token 参数。
甚至使用一些模拟服务。
所有这些，CLI 都替你考虑到了。</p><p translation-origin="off">      This folder contains one file for each of your destination environments,
each exporting simple configuration variables to use in your application.
The files are replaced on-the-fly when you build your app.
You might use a different API endpoint for development than you do for production
or maybe different analytics tokens.
You might even use some mock services.
Either way, the CLI has you covered.</p>

</td></tr><tr><td><p translation-origin="off">      <code>browserslist</code></p>
</td><td><p translation-result="">      一个配置文件，用来在不同的前端工具之间共享<a href="https://github.com/browserslist/browserslist">目标浏览器</a>。</p><p translation-origin="off">      A configuration file to share <a href="https://github.com/browserslist/browserslist">target browsers</a> between different front-end tools.</p>
</td></tr>  <tr><td><p translation-origin="off">      <code>favicon.ico</code></p></td><td><p translation-result="">      每个网站都希望自己在书签栏中能好看一点。
请把它换成你自己的图标。</p><p translation-origin="off">      Every site wants to look good on the bookmark bar.
Get started with your very own Angular icon.</p>
</td></tr><tr><td><p translation-origin="off">      <code>index.html</code></p></td><td><p translation-result="">      这是别人访问你的网站是看到的主页面的 HTML 文件。
大多数情况下你都不用编辑它。
在构建应用时，CLI 会自动把所有 <code>js</code> 和 <code>css</code> 文件添加进去，所以你不必在这里手动添加任何 <code>&lt;script&gt;</code> 或 <code>&lt;link&gt;</code> 标签。</p><p translation-origin="off">      The main HTML page that is served when someone visits your site.
Most of the time you'll never need to edit it.
The CLI automatically adds all <code>js</code> and <code>css</code> files when building your app so you
never need to add any <code>&lt;script&gt;</code> or <code>&lt;link&gt;</code> tags here manually.</p>
</td></tr><tr><td>
<p translation-origin="off">      <code>karma.conf.js</code></p></td><td><p translation-result="">      给<a href="https://karma-runner.github.io">Karma</a>的单元测试配置，当运行 <code>ng test</code> 时会用到它。</p><p translation-origin="off">      Unit test configuration for the <a href="https://karma-runner.github.io">Karma test runner</a>,
used when running <code>ng test</code>.</p>
</td></tr><tr><td><p translation-origin="off">      <code>main.ts</code></p></td><td><p translation-result="">      这是应用的主要入口点。
使用<a href="https://www.angular.cn/guide/glossary#jit">JIT 编译器</a>编译本应用，并启动应用的根模块 <code>AppModule</code>，使其运行在浏览器中。
你还可以使用<a href="https://www.angular.cn/guide/glossary#ahead-of-time-aot-compilation">AOT 编译器</a>，而不用修改任何代码 —— 只要给 <code>ng build</code> 或 <code>ng serve</code> 传入 <code>--aot</code> 参数就可以了。</p><p translation-origin="off">      The main entry point for your app.
Compiles the application with the <a href="https://www.angular.cn/guide/glossary#jit">JIT compiler</a>
and bootstraps the application's root module (<code>AppModule</code>) to run in the browser.
You can also use the <a href="https://www.angular.cn/guide/aot-compiler">AOT compiler</a>
without changing any code by appending the<code>--aot</code> flag to the <code>ng build</code> and <code>ng serve</code> commands.</p></td></tr><tr><td><p translation-origin="off">      <code>polyfills.ts</code></p></td><td><p translation-result="">      不同的浏览器对 Web 标准的支持程度也不同。
腻子脚本（polyfill）能把这些不同点进行标准化。
你只要使用 <code>core-js</code> 和 <code>zone.js</code> 通常就够了，不过你也可以查看<a href="https://www.angular.cn/guide/browser-support">浏览器支持指南</a>以了解更多信息。</p><p translation-origin="off">      Different browsers have different levels of support of the web standards.
Polyfills help normalize those differences.
You should be pretty safe with <code>core-js</code> and <code>zone.js</code>, but be sure to check out
the <a href="https://www.angular.cn/guide/browser-support">Browser Support guide</a> for more information.</p></td></tr>
  <tr><td><p translation-origin="off">      <code>styles.css</code></p></td><td>
<p translation-result="">      这里是你的全局样式。
大多数情况下，你会希望在组件中使用局部样式，以利于维护，不过那些会影响你整个应用的样式你还是需要集中存放在这里。</p><p translation-origin="off">      Your global styles go here.
Most of the time you'll want to have local styles in your components for easier maintenance,
but styles that affect all of your app need to be in a central place.</p>
</td></tr><tr><td>
<p translation-origin="off">      <code>test.ts</code></p></td><td>
<p translation-result="">      这是单元测试的主要入口点。
它有一些你不熟悉的自定义配置，不过你并不需要编辑这里的任何东西。</p><p translation-origin="off">      This is the main entry point for your unit tests.
It has some custom configuration that might be unfamiliar, but it's not something you'll
need to edit.</p></td></tr><tr><td>
<p translation-origin="off">      <code>tsconfig.{app|spec}.json</code></p>
    </td><td>
<p translation-result="">      TypeScript 编译器的配置文件。<code>tsconfig.app.json</code> 是为 Angular 应用准备的，而 <code>tsconfig.spec.json</code> 是为单元测试准备的。</p><p translation-origin="off">      TypeScript compiler configuration for the Angular app (<code>tsconfig.app.json</code>)
and for the unit tests (<code>tsconfig.spec.json</code>).</p>
</td></tr><tr><td>
<p translation-origin="off">      <code>tslint.json</code></p></td><td>
<p translation-result="">      额外的 Linting 配置。当运行 <code>ng lint</code> 时，它会供带有 <a href="http://codelyzer.com/">Codelyzer</a> 的 <a href="https://palantir.github.io/tslint/">TSLint</a> 使用。
Linting 可以帮你们保持代码风格的一致性。</p><p translation-origin="off">      Additional Linting configuration for <a href="https://palantir.github.io/tslint/">TSLint</a> together with
<a href="http://codelyzer.com/">Codelyzer</a>, used when running <code>ng lint</code>.
Linting helps keep your code style consistent.</p></td></tr>  
</tbody>
</table>


