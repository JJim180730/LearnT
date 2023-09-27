#  要求：
#  不能修改被装饰的函数的源代码
#  不能修改被装饰的函数的调用方式
#  满足上面的两种情况下给程序增添功能

#  组成：
#  < 函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖 = 装饰器 >

import time
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("run time %s"%(stop_time-start_time))
    return wrapper


@timer      #语法糖  test=timer(test)
def test():
    time.sleep(3)
    print("in the test")

test()

# 1.test表示的是函数的内存地址
# 2.test()就是调用对在test这个地址的内容，即函数

# 高阶函数：
# 1.把一个函数名当作实参传给另外一个函数（“实参高阶函数”）
# 2.返回值中包含函数名（“返回值高阶函数”）
# 这里面所说的函数名，实际上就是函数的地址，把函数名当做实参，那么也就是说可以把函数传递到另一个函数，然后在另一个函数里面做一些操作。

# 嵌套函数：
# 嵌套函数指的是在函数内部定义一个函数，而不是调用
# 函数只能调用和它同级别以及上级的变量或函数。也就是说：里面的能调用和它缩进一样的和他外部的，而内部的是无法调用的。

# 把test作为参数传递给了timer()，此时，在timer()内部，func = test，接下来，定义了一个wrapper()函数，但并未调用，只是在内存中保存了，并且
# 标签为wrapper。在timer()函数的最后返回wrapper()的地址wrapper。然后再把wrapper赋值给了test，那么此时test已经不是原来的test了，也就是test原来的那些函数体的标签换掉了，换成了wrapper


# 装饰有参函数

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print(stop_time-start_time)
    return deco

@timer
def test(parameter):
    time.sleep(3)
    print("test is running")

test("添加参数")


# 更复杂的装饰器
# 对这两个函数分别统计运行时间，再加一层函数来接受参数，根据嵌套函数的概念，要想执行内函数，就要先执行外函数，才能调用到内函数
import time

def timer(parameter):

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper

@timer(parameter='task1')
def task1():
    time.sleep(2)
    print("in the task1")

@timer(parameter='task2')
def task2():
    time.sleep(2)
    print("in the task2")

task1()
task2()


