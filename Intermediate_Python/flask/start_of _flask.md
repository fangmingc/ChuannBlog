## 请求到达flask之前
- flask项目本质上也是socket的服务端，所以启动flask项目就是启动socket服务，开启阻塞，等待请求数据
- 接收到请求数据，开始处理请求，将处理好的请求封装到request，传递给flask框架

### flask项目的启动
- app.run()
- 

### 请求接入，传递到flask框架
