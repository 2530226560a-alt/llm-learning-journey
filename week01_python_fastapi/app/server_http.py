## web应用程序：遵循 http 协议
## 定义一个web 应用程序去测试 http 协议

import socket
    # 创建一个 socket 对象
socket_server = socket.socket()
    # 绑定一个地址和端口号
socket_server.bind(('127.0.0.1', 8080))
socket_server.listen(5)

while 1:
    # conn 表示一个管道，双向的，可以用于发送或者接受信息
        # 阻塞等待客户端连接
    conn,addr = socket_server.accept()
        # 接收客户端发送过来的数据   
    data = conn.recv(1024)  
    print("收到客户端发送过来的数据：", data)

    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n{"user_id": "123", "answer": "testanswer"", "model": "gpt-3.5-turbo", "tokens_used": 10}')
    conn.close()