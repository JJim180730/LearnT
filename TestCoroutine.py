# 1.简介
# 协程(Coroutine) : 是单线程下的并发 , 又称微线程 , 纤程 . 协程是一种用户态的轻量级线程 , 即协程有用户自己控制调度

# 协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。

# 协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态

# 使用协程的优缺点

# 优点 :

# 协程的切换开销更小 , 属于程序级别的切换 , 更加轻量级
# 单线程内就可以实现并发的效果 , 最大限度利用CPU
# 缺点 :

# 协程的本质是单线程下 , 无法利用多核 , 可以是一个程序开启多个进程 , 每个进程内开启多个线程 , 每个线程内开启协程
# 协程指的是单个线程 , 因而一旦协程出现阻塞 将会阻塞整个线程

# Greenlet
# greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()      #到这里切换到gr2，执行test2（）
    print(34)
    gr2.switch()      #切换到上次gr2运行的位置

def test2():
    print(56)
    gr1.switch()      #切换到上次gr1运行的位置
    print(78)

gr1 = greenlet(test1)      #启动一个协程gr1
gr2 = greenlet(test2)      #启动一个协程gr2

gr1.switch()        #开始运行gr1

# Gevent
# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('阻塞时间最长，最后运行')

def bar():
    print('running in bar')
    gevent.sleep(1)
    print('foo（）还在阻塞，这里第二个运行')

def func3():
    print("running in func3 ")
    gevent.sleep(0)
    print("其它两个还在IO阻塞先运行")

#创建协程实例
gevent.joinall([
    gevent.spawn(foo), #生成，
    gevent.spawn(bar),
    gevent.spawn(func3),
])

#遇到IO自动切换




# 结果：
# Running in foo
# running in bar
# running in func3 
# 其它两个还在IO阻塞先运行
# foo（）还在阻塞，这里第二个运行
# 阻塞时间最长，最后运行