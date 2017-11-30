## 邮件

- 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
- 收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。
- 特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录：

### 邮件的流程
- MUA(Mail User Agent)，邮件用户代理
- MTA(Mail Transfer Agent)，邮件传输代理
- MDA(Mail Delivery Agent)，邮件投递代理

- 假设通过sender@163.com给receiver@qq.com发送邮件
	- 在网易提供的邮件软件客户端(MUA)编写好邮件
	- 邮件传输到网易服务器(MTA)
	- 可能经过了若干MTA，最后抵达腾讯服务器(MTA)
	- 腾讯服务器识别到收件人属于自己的范围，传输到MDA的数据库
	- 对方登录腾讯的邮件软件客户端(MUA)，从MDA获取自己的邮件
- 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

### python下的邮件发送
发送邮件使用smtplib，组装邮件使用email，都是python的标准库。


#### 

```
send: 'ehlo [169.254.50.122]\r\n'
reply: b'250-mail\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-AUTH LOGIN PLAIN\r\n'
reply: b'250-AUTH=LOGIN PLAIN\r\n'
reply: b'250-coremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UFwcXtdUCa0xDrUUUUj\r\n'
reply: b'250-STARTTLS\r\n'
reply: b'250 8BITMIME\r\n'
reply: retcode (250); Msg: b'mail\nPIPELINING\nAUTH LOGIN PLAIN\nAUTH=LOGIN PLAIN\ncoremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UFwcXtdUCa0xDrUUUUj\nSTARTTLS\n8BITMIME'
send: 'AUTH PLAIN AHljZ19nenl4MkAxNjMuY29tAGNodWFuZ3Vhbmc5MjU=\r\n'
reply: b'235 Authentication successful\r\n'
reply: retcode (235); Msg: b'Authentication successful'
send: 'mail FROM:<ycg_gzyx2@163.com>\r\n'
reply: b'250 Mail OK\r\n'
reply: retcode (250); Msg: b'Mail OK'
send: 'rcpt TO:<906537842@qq.com>\r\n'
reply: b'250 Mail OK\r\n'
reply: retcode (250); Msg: b'Mail OK'
send: 'data\r\n'
reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
data: (354, b'End data with <CR><LF>.<CR><LF>')
send: b'Content-Type: text/plain; charset="utf-8"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: base64\r\nFrom: =?utf-8?q?mail=2E163?= <ycg_gzyx2@163.com>\r\nTo: =?utf-8?q?mail=2Eqq?= <906537842@qq.com>\r\nSubject: =?utf-8?b?56ys5LqM5bCB?=\r\n\r\naGVsbG8sIHNlbmQgYnkgUHl0aG9uLi4u\r\n.\r\n'
reply: b'250 Mail OK queued as smtp13,EcCowAAnd9cecxNa9JEZAw--.61642S2 1511224096\r\n'
reply: retcode (250); Msg: b'Mail OK queued as smtp13,EcCowAAnd9cecxNa9JEZAw--.61642S2 1511224096'
data: (250, b'Mail OK queued as smtp13,EcCowAAnd9cecxNa9JEZAw--.61642S2 1511224096')
send: 'quit\r\n'
reply: b'221 Bye\r\n'
reply: retcode (221); Msg: b'Bye'
```

