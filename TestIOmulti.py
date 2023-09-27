# blocking和non-blocking的区别
# 调用blocking IO会一直block住对应的进程直到操作完成，而non-blocking IO在kernel还准备数据的情况下会立刻返回。

# synchronous IO和asynchronous IO的区别
# 在说明synchronous IO和asynchronous IO的区别之前，需要先给出两者的定义。POSIX的定义是这样子的：
# - A synchronous I/O operation causes the requesting process to be blocked until that I/O operation completes;
# - An asynchronous I/O operation does not cause the requesting process to be blocked;

# 两者的区别就在于synchronous IO做”IO operation”的时候会将process阻塞。按照这个定义，之前所述的blocking IO，non-blocking IO，IO multiplexing都属于synchronous IO。

# 有人会说，non-blocking IO并没有被block啊。这里有个非常“狡猾”的地方，定义中所指的”IO operation”是指真实的IO操作，就是例子中的recvfrom这个system call。non-blocking IO在执行recvfrom这个system call的时候，如果kernel的数据没有准备好，这时候不会block进程。但是，当kernel中数据准备好的时候，recvfrom会将数据从kernel拷贝到用户内存中，这个时候进程是被block了，在这段时间内，进程是被block的。

# 而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，告诉进程说IO完成。在这整个过程中，进程完全没有被block。

# I/O 多路复用之select、poll、epoll详解
# select，poll，epoll都是IO多路复用的机制。I/O多路复用就是通过一种机制，一个进程可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。但select，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的，而异步I/O则无需自己负责进行读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。（这里啰嗦下）

# select
# 1
# select(rlist, wlist, xlist, timeout=None)
# select 函数监视的文件描述符分3类，分别是writefds、readfds、和exceptfds。调用后select函数会阻塞，直到有描述副就绪（有数据 可读、可写、或者有except），或者超时（timeout指定等待时间，如果立即返回设为null即可），函数返回。当select函数返回后，可以 通过遍历fdset，来找到就绪的描述符。

# select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点。select的一 个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，可以通过修改宏定义甚至重新编译内核的方式提升这一限制，但 是这样也会造成效率的降低

# poll
# 1
# int poll (struct pollfd *fds, unsigned int nfds, int timeout);
# 不同与select使用三个位图来表示三个fdset的方式，poll使用一个 pollfd的指针实现。

# struct pollfd {
#     int fd; /* file descriptor */
#     short events; /* requested events to watch */
#     short revents; /* returned events witnessed */
# };
# pollfd结构包含了要监视的event和发生的event，不再使用select“参数-值”传递的方式。同时，pollfd并没有最大数量限制（但是数量过大后性能也是会下降）。 和select函数一样，poll返回后，需要轮询pollfd来获取就绪的描述符。

# 从上面看，select和poll都需要在返回后，通过遍历文件描述符来获取已经就绪的socket。事实上，同时连接的大量客户端在一时刻可能只有很少的处于就绪状态，因此随着监视的描述符数量的增长，其效率也会线性下降。

# epoll是在2.6内核中提出的，是之前的select和poll的增强版本。相对于select和poll来说，epoll更加灵活，没有描述符限制。epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个事件表中，这样在用户空间和内核空间的copy只需一次

# epoll操作过程需要三个接口，分别如下：


# int epoll_create(int size)；//创建一个epoll的句柄，size用来告诉内核这个监听的数目一共有多大
# int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)；
# int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
# 1. int epoll_create(int size);
# 创建一个epoll的句柄，size用来告诉内核这个监听的数目一共有多大，这个参数不同于select()中的第一个参数，给出最大监听的fd+1的值，参数size并不是限制了epoll所能监听的描述符最大个数，只是对内核初始分配内部数据结构的一个建议。
# 当创建好epoll句柄后，它就会占用一个fd值，在linux下如果查看/proc/进程id/fd/，是能够看到这个fd的，所以在使用完epoll后，必须调用close()关闭，否则可能导致fd被耗尽。

# 2. int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)；
# 函数是对指定描述符fd执行op操作。
# - epfd：是epoll_create()的返回值。
# - op：表示op操作，用三个宏来表示：添加EPOLL_CTL_ADD，删除EPOLL_CTL_DEL，修改EPOLL_CTL_MOD。分别添加、删除和修改对fd的监听事件。
# - fd：是需要监听的fd（文件描述符）
# - epoll_event：是告诉内核需要监听什么事

# 3. int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
# 等待epfd上的io事件，最多返回maxevents个事件。
# 参数events用来从内核得到事件的集合，maxevents告之内核这个events有多大，这个maxevents的值不能大于创建epoll_create()时的size，参数timeout是超时时间（毫秒，0会立即返回，-1将不确定，也有说法说是永久阻塞）。该函数返回需要处理的事件数目，如返回0表示已超时

#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import socket, logging
import select, errno

logger = logging.getLogger("network-server")

def InitLog():
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("network-server.log")
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)


if __name__ == "__main__":
    InitLog()

    try:
        # 创建 TCP socket 作为监听 socket
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as  msg:
        logger.error("create socket failed")

    try:
        # 设置 SO_REUSEADDR 选项
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as  msg:
        logger.error("setsocketopt SO_REUSEADDR failed")

    try:
        # 进行 bind -- 此处未指定 ip 地址，即 bind 了全部网卡 ip 上
        listen_fd.bind(('', 2003))
    except socket.error as  msg:
        logger.error("bind failed")

    try:
        # 设置 listen 的 backlog 数
        listen_fd.listen(10)
    except socket.error as  msg:
        logger.error(msg)

    try:
        # 创建 epoll 句柄
        epoll_fd = select.epoll()
        
        # 向 epoll 句柄中注册 监听 socket 的 可读 事件
        epoll_fd.register(listen_fd.fileno(), select.EPOLLIN)
    except select.error as  msg:
        logger.error(msg)

    connections = {}
    addresses = {}
    datalist = {}
    while True:
        # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
        epoll_list = epoll_fd.poll()

        for fd, events in epoll_list:
            # 若为监听 fd 被激活
            if fd == listen_fd.fileno():
                # 进行 accept -- 获得连接上来 client 的 ip 和 port，以及 socket 句柄
                conn, addr = listen_fd.accept()
                logger.debug("accept connection from %s, %d, fd = %d" % (addr[0], addr[1], conn.fileno()))
                # 将连接 socket 设置为 非阻塞
                conn.setblocking(0)
                # 向 epoll 句柄中注册 连接 socket 的 可读 事件
                epoll_fd.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)
                # 将 conn 和 addr 信息分别保存起来
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
            elif select.EPOLLIN & events:
                # 有 可读 事件激活
                datas = ''
                while True:
                    try:
                        # 从激活 fd 上 recv 10 字节数据
                        data = connections[fd].recv(10)
                        # 若当前没有接收到数据，并且之前的累计数据也没有
                        if not data and not datas:
                            # 从 epoll 句柄中移除该 连接 fd
                            epoll_fd.unregister(fd)
                            # server 侧主动关闭该 连接 fd
                            connections[fd].close()
                            logger.debug("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
                            break
                        else:
                            # 将接收到的数据拼接保存在 datas 中
                            datas += data
                    except socket.error as  msg:
                        # 在 非阻塞 socket 上进行 recv 需要处理 读穿 的情况
                        # 这里实际上是利用 读穿 出 异常 的方式跳到这里进行后续处理
                        if msg.errno == errno.EAGAIN:
                            logger.debug("%s receive %s" % (fd, datas))
                            # 将已接收数据保存起来
                            datalist[fd] = datas
                            # 更新 epoll 句柄中连接d 注册事件为 可写
                            epoll_fd.modify(fd, select.EPOLLET | select.EPOLLOUT)
                            break
                        else:
                            # 出错处理
                            epoll_fd.unregister(fd)
                            connections[fd].close()
                            logger.error(msg)
                            break
            elif select.EPOLLHUP & events:
                # 有 HUP 事件激活
                epoll_fd.unregister(fd)
                connections[fd].close()
                logger.debug("%s, %d closed" % (addresses[fd][0], addresses[fd][1]))
            elif select.EPOLLOUT & events:
                # 有 可写 事件激活
                sendLen = 0
                # 通过 while 循环确保将 buf 中的数据全部发送出去
                while True:
                    # 将之前收到的数据发回 client -- 通过 sendLen 来控制发送位置
                    sendLen += connections[fd].send(datalist[fd][sendLen:])
                    # 在全部发送完毕后退出 while 循环
                    if sendLen == len(datalist[fd]):
                        break
                # 更新 epoll 句柄中连接 fd 注册事件为 可读
                epoll_fd.modify(fd, select.EPOLLIN | select.EPOLLET)
            else:
                # 其他 epoll 事件不进行处理
                continue