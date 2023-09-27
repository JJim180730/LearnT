# Python中的多线程无法利用多核优势 , 所以如果我们想要充分地使用多核CPU的资源 , 那么就只能靠多进程了
# multiprocessing模块中提供了Process , Queue , Pipe , Lock , RLock , Event , Condition等组件 , 与threading模块有很多相似之处

from multiprocessing import Process
import time

def func(name):
    time.sleep(2)
    print('hello',name)

if __name__ == '__main__':
    p = Process(target=func,args=('derek',))
    p.start()
    # p.join()
    print('end...')


# 进程间通讯 
# 不同进程间内存是不共享的，要想实现两个进程间的数据交换。进程间通信有两种主要形式 , 队列和管道
from multiprocessing import Process, Queue   #Queue是进程排列

def f(test):
    print("put 22 in the queue")
    test.put('22')   #通过创建的子进程往队列添加数据，实线父子进程交互

if __name__ == '__main__':
    q = Queue()      #父进程
    q.put("11")
    print("put 11 in the queue")
    p = Process(target=f, args=(q,))   #子进程
    p.start()
    p.join()

    print("取到：",q.get_nowait())
    print("取到：",q.get_nowait())

#父进程在创建子进程的时候就把q克隆一份给子进程
#通过pickle序列化、反序列化，来达到两个进程之间的交互


# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
from multiprocessing import Process, Pipe

def f(conn):
    conn.send('11')
    conn.send('22')
    print("from parent:",conn.recv())
    print("from parent:", conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()   #生成管道实例，可以互相send（）和recv（）

    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())      # prints "11"
    print(parent_conn.recv())      # prints "22"
    parent_conn.send("33")         # parent 发消息给 child
    parent_conn.send("44")
    p.join()



# Manager
# 进程之间是相互独立的 ,Queue和pipe只是实现了数据交互，并没实现数据共享，Manager可以实现进程间数据共享 。

# Manager还支持进程中的很多操作 , 比如Condition , Lock , Namespace , Queue , RLock , Semaphore等
from multiprocessing import Process, Manager
import os

def f(d, l):
    d[os.getpid()] =os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  #{} #生成一个字典，可在多个进程间共享和传递

        l = manager.list(range(5))     #生成一个列表，可在多个进程间共享和传递
        p_list = []
        for i in range(2):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list: #等待结果
            res.join()
        print(d)
        print(l)

# lock
from multiprocessing import Process, Lock

def f(l, i):
    #l.acquire()
    print('hello world', i)
    #l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()     #要把lock传到函数的参数l
        
#lock防止在屏幕上打印的时候会乱

# 进程池
# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。

# 进程池中有以下几个主要方法：

# apply：从进程池里取一个进程并执行
# apply_async：apply的异步版本
# terminate:立刻关闭线程池
# join：主进程等待所有子进程执行完毕，必须在close或terminate之后
# close：等待所有进程结束后，才关闭线程池

from  multiprocessing import Process, Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':    #多进程，必须加这一句（windows系统）
    pool = Pool(processes=3) #允许进程池同时放入3个进程
    print("主进程",os.getpid())
    
    for i in range(10):       
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #callback=回调，执行完Foo(),接着执行Bar()
        # pool.apply(func=Foo, args=(i,)) #串行
        
    print('end')
    pool.close()
    pool.join()   #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。必须先close(),再join（）
