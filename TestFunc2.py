# 1.普通参数
def func(name):     #name是形式参数
    print(name)      #函数体

func('derek')       #执行函数，'derek'是传入的实参

# 2.默认参数
# 定义了默认参数后，在函数调用时不需要再传入，默认参数放在最后面


def info(name,age,country = 'CN'):   #country定义了一个默认参数
    print('姓名:',name)
    print('年龄:',age)
    print('国籍：',country)

info('derek',22)     #调用时，没穿实参countrty，就用默认的参数

# 3.关键参数
#  正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可，但记住一个要求就是，关键参数必须放在位置参数之后


def info(name,age,country = 'CN'):
    print('姓名:',name)
    print('年龄:',age)
    print('国籍：',country)

info(age=22,name='derek')   #使用关键参数，可以不按顺序


# 4.*args
def info(name,age,*args):     #*args会把多传入的参数变成一个元祖形式
    print(name, age,args)

# info("derek","22","CN","Python")     #derek 22 ('CN', 'Python')

# 5.**kwargs
def info(name, *args, **kwargs):  # **kwargs 会把多传入的参数变成一个dict形式
    print(name, args)    #derek (22, 'CN', 'Python')
    print(kwargs)        #{'sex': 'Male', 'province': 'HeBei'}

# info("derek", 22, "CN", "Python", sex="Male", province="HeBei")


# 6.局部变量
# 作用域在函数内部，不影响外部

name = 'derek1'

def change_name(name):
    print('before change:',name)
    name = 'derek2'
    print('after change:',name)

change_name(name)
print('最后还是没改',name)


# 结果：
# before change: derek1
# after change: derek2
# 最后还是没改 derek1

# 递归函数
# 如果一个函数在内部调用自身，那么这个函数就叫做递归函数。

# 1. 必须有一个明确的结束条件；

# 2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少；

# 3.递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出


#递归实现阶乘n! = (n-1)! × n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# 结果：120

# # 过程：
# factorial(5)                        # 第 1 次调用使用 5
# 5 * factorial(4)                    # 第 2 次调用使用 4
# 5 * (4 * factorial(3))              # 第 3 次调用使用 3
# 5 * (4 * (3 * factorial(2)))        # 第 4 次调用使用 2
# 5 * (4 * (3 * (2 * factorial(1))))  # 第 5 次调用使用 1 
# 5 * (4 * (3 * (2 * 1)))             # 从第 5 次调用返回
# 5 * (4 * (3 * 2))                   # 从第 4 次调用返回
# 5 * (4 * 6)                         # 从第 3次调用返回
# 5 * 24                              # 从第 2 次调用返回
# 120                                 # 从第 1 次调用返回


# 高阶函数
# 满足下列条件之一就可称函数为高阶函数
# 某一函数当做参数传入另一个函数中
# 函数的返回值包含一个或多个函数

#简单的高阶函数

def func():
    print('in the func')
    return foo()
def foo():
    print('in the foo()')
    return 666

res = func()
print(res)

# 结果：
# in the func
# in the foo()
# 666

#  map()函数
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回


def func(x):
    return x * x
a= map(func,range(1,10))
print(list(a))

# 结果：
# [1, 4, 9, 16, 25, 36, 49, 64, 81]


# reduce()函数
# reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值

from functools import reduce
def f(x,y):
    return x + y
a = reduce(f,[1,3,5,7,9,10])
print(a)

# 结果：
# 35


# filter()函数
# filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list


def is_odd(x):
    return x % 2 == 1
a = filter(is_odd,[1,2,3,4,5,6,7,8])
print(list(a))

# 结果：[1, 3, 5, 7]

# 匿名函数lambda
# lambda 函数是一种快速定义单行的最小函数，可以用在任何需要函数的地方

# 优点：让代码更加精简，不需要考虑命名的问题


#常规函数
def fun(x,y):
    return x + y

#匿名函数
a = lambda x,y:x + y
print(fun(2,3))


#  内嵌函数和作用域
# 定义：在一个函数体内创建另外一个函数，这种函数就叫内嵌函数

# 实例

def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()

foo()


# 结果：
# in the foo
# in the bar


# 局部作用域和全局作用域的访问顺序


x = 0
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()
print(x)


# 结果：
# 3
# 0
