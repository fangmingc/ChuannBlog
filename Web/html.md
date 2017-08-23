# html

## 初识html
html是HyperTxt Makeup Language（超文本标记语言）的简称。  
HyperText is text displayed on a computer or device that provides access to 
other text through links, also known as “hyperlinks”.  

### <!DOCTYPE html>
浏览器需要知道网页是何种标准的html语言编写的以便更好的展示页面，即使不写这一行声明，页面似乎也能正常打开，但是这是有风险的，如果遇到旧标准的浏览器或者未来其他版本的html标准，就会出错。  
通常这是由html代码的第一行声明。
### <html></html>
仅有声明html标准是不够的，浏览器还需要知道文件的那一部分需要使用html标准解释。  
这个时候使用<html>  </html>标记，包含在其中的内容都会被浏览器解释，超出的部分则不能确保发生了何事。
### html标准化的语言
![](https://s3.amazonaws.com/codecademy-content/courses/web-101/htmlcss1-diagram__htmlanatomy.svg)  
- 尖括号<> html语言大量使用角括号
- html元素：尖括号之间的内容就是html元素
- 开始标签，第一个html标签用于开始一个html元素
- 结束标签，第二个html标签用于结束一个html元素，结束标签需要在内部的前方使用一个/符号
- 图中的<p>表示段落元素

### <head></head>
该标签包包含了一些页面的信息，并且不会显示在web页面
那么哪些内容会被包含在<head>标签内？
### <title></title>
浏览器标签页面的标题就是由这个标签内的内容展示的。
### <body></body>
The Body
We've added some HTML, but still haven't seen any results in the web browser to the right. Why is that?

Before we can add content that a browser will display, we have to add a body to the HTML file. Once the file has a body, many different types of content can be added within the body, like text, images, buttons, and much more.


