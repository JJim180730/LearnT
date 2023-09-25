# Python 提供了两个级别访问的网络服务。：

# 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统 Socket 接口的全部方法。
# 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。
# 什么是 Socket?
# Socket 又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯

# socket()函数
# Python 中，我们用 socket（）函数来创建套接字，语法格式如下：

# socket.socket([family[, type[, proto]]])
# 参数
# family: 套接字家族可以使 AF_UNIX 或者 AF_INET   AF_INET uses the TCP/IP protocol. 
# AF_UNIX creates filesystem objects and it only works between processes on the same host. AF_UNIX is much faster than AF_INET


# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# sock_stream 是有保障的(即能保证数据正确传送到对方)面向连接的SOCKET，多用于资料(如文件)传送。
# sock_dgram 是无保障的面向消息的socket ， 主要用于在网络上发广播信息。
# SOCK_STREAM是基于TCP的，数据传输比较有保障。SOCK_DGRAM是基于UDP的，专门用于局域网，基于广播SOCK_STREAM 是数据流,一般是tcp/ip协议的编程,SOCK_DGRAM分是数据抱,是udp协议网络编程

# protocol: 一般不填默认为0.

server.py