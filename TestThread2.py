# 基本概念
# 1.进程
#       定义:　 进程就是一个程序在一个数据集上的一次动态执行过程。

# 　　组成：  进程一般由程序、数据集、进程控制块三部分组成。

# 　　程序：  我们编写的程序用来描述进程要完成哪些功能以及如何完成；

# 　　数据集：　则是程序在执行过程中所需要使用的资源；

# 　　进程控制块:　用来记录进程的外部特征，描述进程的执行变化过程，系统可以利用它来控制和管理进程，它是系统感知进程存在的唯一标志

# 2.线程
#        线程的出现是为了降低上下文切换的消耗，提高系统的并发性，并突破一个进程只能干一样事的缺陷，使到进程内并发成为可能。

# 　　线程也叫轻量级进程，它是一个基本的CPU执行单元，也是程序执行过程中的最小单元

# 　   组成：由线程ID、程序计数器、寄存器集合和堆栈共同组成。

# 　　线程的引入减小了程序并发执行时的开销，提高了操作系统的并发性能。线程没有自己的系统资源

# 3.线程与进程的区别
# 线程是执行的指令集 , 进程是资源的集合
# 线程的启动速度要比进程的启动速度要快
# 两个线程的执行速度是一样的
# 进程与线程的运行速度是没有可比性的
# 线程共享创建它的进程的内存空间 , 进程的内存是独立的
# 两个线程共享的数据都是同一份数据 , 两个子进程的数据不是共享的 , 而且数据是独立的
# 同一个进程的线程之间可以直接交流 , 同一个主进程的多个子进程之间是不可以进行交流 , 如果两个进程之间需要通信 , 就必须要通过一个中间代理来实现
# 一个新的线程很容易被创建 , 一个新的进程创建需要对父进程进行一次克隆
# 一个线程可以控制和操作同一个进程里的其他线程 , 线程与线程之间没有隶属关系 , 但是进程只能操作子进程
# 改变主线程 , 有可能会影响到其他线程的行为 , 但是对于父进程的修改是不会影响子进程
# 4.同步和异步
#         同步就是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到收到返回信息才继续执行下去；

# 　    异步是指进程不需要一直等下去，而是继续执行下面的操作，不管其他进程的状态。当有消息返回时系统会通知进程进行处理，这样可以提高执行的效率。

#        举个例子，打电话时就是同步通信，发短息时就是异步通信

# 5.并行和并发
#         并行指系统具有处理多个任务(动作)的能力

#        并发是指系统具有同时处理多个任务(动作)的能力

#  6.阻塞与非阻塞
#         阻塞调用是指调用结果返回之前，当前线程会被挂起（如遇到io操作）。函数只有在得到结果之后才会将阻塞的线程激活。

#         非阻塞和阻塞的概念相对应，指在不能立刻得到结果之前也会立刻返回，同时该函数不会阻塞当前线程

import threading
import time

def run(n):         #定义线程要运行的函数
    print('task',n)
    time.sleep(2)

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(1,))          #生成一个线程
    t2 = threading.Thread(target=run,args=(2,))
    t1.start()
    t2.start()

print('I am main thread')                #主线程

#这个进程里面有三个线程，1个主线程，t1,t2两个子线程
#子线程和主线程是同步开启的，主线程结束后，要等子线程全部结束后，进程才会关闭函数调用


# 类继承调用
import threading,time

class MyThread(threading.Thread):   #继承threading,Thread模块
    def __init__(self,n):
        super(MyThread, self).__init__()    #继承父类
        self.n = n

    def run(self):                 #必须用run
        print('task',self.n)
        time.sleep(2)

t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t2.start()

print('I am main thread')
print(t1.is_alive())       #返回线程是否活动的。
print(t1.getName())        #返回线程名。
t1.setName('我是T1')       #设置线程名。
print(t1.getName())
print(threading.currentThread())     #查看当前线程是主线程（mainThread）还是子线程(Thread)
print(threading.activeCount())       #返回正在运行的线程数量


# 结果：
# task 1
# task 2
# I am main thread
# True
# Thread-1
# 我是T1
# <_MainThread(MainThread, started 9580)>
# 3

# Process finished with exit code 0


# Join和setDaemon
# 主线程 : 当一个程序启动时 , 就有一个进程被操作系统创建 , 与此同时一个线程也立刻运行 , 该线程通常叫做程序的主线程

# 子线程 : 因为程序是开始时就执行的 , 如果你需要再创建线程 , 那么创建的线程就是这个主线程的子线程

# join的作用:是保证当前线程执行完成后，再执行其它线程

import threading
import time

def run(n):
    print("task ",n )
    time.sleep(2)

start_time = time.time()
t_objs = []    #存线程实例

for i in range(50):        #生成50个线程
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t)  #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:      #循环线程实例列表，等待所有线程执行完毕
    t.join()

print("---all threads has finished...")
print("cost:",time.time() - start_time)

# setDaemon

# 将线程声明为守护线程，必须在start() 方法调用之前设
# setDaemon(),只要主线程完成了，不管子线程是否完成，都要和主线程一起退出
import threading
import time

def run(n):
    print('task',n)
    time.sleep(2)
    print('i am 子线程')     #主线程结束，setDaemon不管有没有运行完都会被销毁

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(2,))
    t1.setDaemon(True)   #设置守护线程,放在start之前
    t1.start()
    t2.setDaemon(True)
    t2.start()

print('I am main thread')

# 线程锁(互斥锁Mutex)
# lock:如果有多个进程对同一文件进行修改 , 就会造成错乱 , 所以我们为了保护文件数据的安全 , 就需要给其进行加锁,join为整体串行 , lock为局部串行

# Rlock:在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁，因为系统判断这部分资源都正在使用，所有这两个线程在无外力作用下将一直等待下去。

#            Rlock就是解决死锁的问题

import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    print('--get num:',num )
    time.sleep(1)
    lock.acquire() #修改数据前加锁
    num  -=1 #对此公共变量进行-1操作
    lock.release() #修改后释放

num = 100  #设定一个共享变量
thread_list = []
lock = threading.Lock() #生成全局锁
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

print('final num:', num )


# semaphore(信号量)
import threading, time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()
while threading.active_count() != 1:
    pass
else:
    print('----all threads done---')


# queue(队列)
import queue
#queue
#主要作用：解耦
#提高运行效率

q =queue.Queue()    #生成一个队列对象   先入先出
q.put('1')          #put item into the queue
q.put('2')
q.put('3')

q.qsize()          #看队列大小
q.get()            #从队列中取

q.get(block=True, timeout=None)  #取不到数据，默认阻塞，timeout设置阻塞时间
q.get_nowait()      #如果队列为空，取不到数据，抛出异常，不会阻塞卡主
q = queue.Queue(maxsize=3)         #maxsize可以设置队列的大小，最多允许存三个
q = queue.PriorityQueue           #优先级
print(q.full())       #判断队列是否有数据  返回blue值
print(q.empty())      #判断队列是否是空    返回blue值

# 生产者消费者模型
# 为什么要使用生产者和消费者模式

# 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

# 什么是生产者消费者模式

# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

import threading,time
import queue

q = queue.Queue(maxsize=5)       #设置maxsize=5，防止生产过快

def Producer(name):    #生产者
    count = 1
    while True:
        q.put("面包%s" % count)
        print("%s生产了面包%s"%(name,count))
        count +=1
        time.sleep(0.1)

def  Consumer(name):         #消费者
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(1)

#生成多个线程
p = threading.Thread(target=Producer,args=("derek",))
c = threading.Thread(target=Consumer,args=("chihuo1",))
c1 = threading.Thread(target=Consumer,args=("chihou2",))

p.start()
c.start()
c1.start()