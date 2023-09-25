# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.w3cschool.cn

# 用户输入数字
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')

# # 求和
# sum = float(num1) + float(num2)

# # 显示计算结果
# print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


# print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))

# num = float(input('请输入一个数字： '))
# num_sqrt = num ** 0.5
# print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

# import cmath

# num = int(raw_input("请输入一个数字: "))
# num_sqrt = cmath.sqrt(num)
# print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供

# 导入 cmath(复杂数学运算) 模块
# import cmath

# a = float(input('输入 a: '))
# b = float(input('输入 b: '))
# c = float(input('输入 c: '))

# # 计算
# d = (b**2) - (4*a*c)

# # 两种求解方式
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)

# print('结果为 {0} 和 {1}'.format(sol1,sol2))

# a = float(input('输入三角形第一边长: '))
# b = float(input('输入三角形第二边长: '))
# c = float(input('输入三角形第三边长: '))

# # 计算半周长
# s = (a + b + c) / 2

# # 计算面积
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('三角形面积为 %0.2f' %area)

# #生成 0 ~ 9 之间的随机数# 导入 random(随机数) 模块
# import random
# print(random.randint(0,9))

# # 用户输入摄氏温度

# # 接收用户收入
# celsius = float(input('输入摄氏温度: '))

# # 计算华氏温度
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))


# # 用户输入

# x = input('输入 x 值: ')
# y = input('输入 y 值: ')

# # 创建临时变量，并交换
# temp = x
# x = y
# y = temp

# print('交换后 x 的值为: {}'.format(x))
# print('交换后 y 的值为: {}'.format(y))

# # 用户输入

# x = input('输入 x 值: ')
# y = input('输入 y 值: ')

# # 不使用临时变量
# x,y = y,x

# print('交换后 x 的值为: {}'.format(x))
# print('交换后 y 的值为: {}'.format(y))

# 用户输入数字

# num = float(input("输入一个数字: "))
# if num > 0:
#    print("正数")
# elif num == 0:
#    print("零")
# else:
#    print("负数")


# # 内嵌 if 语句

# num = float(input("输入一个数字: "))
# if num >= 0:
#    if num == 0:
#        print("零")
#    else:
#        print("正数")
# else:
#    print("负数")


# # Python 判断奇数偶数
# # 如果是偶数除于 2 余数为 0
# # 如果余数为 1 则为奇数

# num = int(input("输入一个数字: "))
# if (num % 2) == 0:
#    print("{0} 是偶数".format(num))
# else:
#    print("{0} 是奇数".format(num))


# year = int(input("输入一个年份: "))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))


# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass

#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass

#     return False

# # 测试字符串和数字
# print(is_number('foo'))   # False
# print(is_number('1'))     # True
# print(is_number('1.3'))   # True
# print(is_number('-1.37')) # True
# print(is_number('1e3'))   # True

# # 测试 Unicode
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四')) # True
# # 版权号
# print(is_number('©'))  # False


# # 最简单的
# print(max(1, 2))
# print(max('a', 'b'))
 
# # 也可以对列表和元组使用
# print(max([1,2]))
# print(max((1,2)))

# # 更多实例
# print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
# print("-20, 100, 400最大值为: ", max(-20, 100, 400))
# print("-80, -20, -10最大值为: ", max(-80, -20, -10))
# print("0, 100, -400最大值为:", max(0, 100, -400))


# # Python 程序用于检测用户输入的数字是否为质素

# # 用户输入数字
# num = int(input("请输入一个数字: "))

# # 质素大于 1
# if num > 1:
#    # 查看因子
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"不是质素")
#            print(i,"乘于",num//i,"是",num)
#            break
#    else:
#        print(num,"是质素")
       
# # 如果输入的数字小于或等于 1，不是质素
# else:
#    print(num,"不是质素")


# # 通过用户输入数字计算阶乘

# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))
# factorial = 1

# # 查看数字是负数，0 或 正数
# if num < 0:
#    print("抱歉，负数没有阶乘")
# elif num == 0:
#    print("0 的阶乘为 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("%d 的阶乘为 %d" %(num,factorial))


# # 九九乘法表
# for i in range(1, 10):
#         for j in range(1, i+1):
#             print('{}x{}={}\t'.format(i, j, i*j), end='')
#         print()


# # Python 斐波那契数列实现

# # 获取用户输入数据
# nterms = int(input("你需要几项？"))

# # 第一和第二项
# n1 = 0
# n2 = 1
# count = 2

# # 判断输入的值是否合法
# if nterms <= 0:
#    print("请输入一个正整数。")
# elif nterms == 1:
#    print("斐波那契数列：")
#    print(n1)
# else:
#    print("斐波那契数列：")
#    print(n1,",",n2,end=" , ")
#    while count < nterms:
#        nth = n1 + n2
#        print(nth,end=" , ")
#        # 更新值
#        n1 = n2
#        n2 = nth
#        count += 1


# # Python 检测用户输入的数字是否为阿姆斯特朗数

# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))

# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))

# # 检测
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** n
#    temp //= 10

# # 输出结果
# if num == sum:
#    print(num,"是阿姆斯特朗数")
# else:
#    print(num,"不是阿姆斯特朗数")


# # 获取指定期间内的阿姆斯特朗数
# # 获取用户输入数字
# lower = int(input("最小值: "))
# upper = int(input("最大值: "))

# for num in range(lower,upper + 1):
#    # 初始化 sum
#    sum = 0
#    # 指数
#    n = len(str(num))

#    # 检测
#    temp = num
#    while temp > 0:
#        digit = temp % 10
#        sum += digit ** n
#        temp //= 10

#    if num == sum:
#        print(num)

# # 实现十进制转二进制、八进制、十六进制
# # 获取用户输入十进制数
# dec = int(input("输入数字："))

# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))

# # 实现ASCII码与字符相互转换
# # 用户输入字符
# c = input("请输入一个字符: ")

# # 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))


# print( c + " 的ASCII 码为", ord(c))
# print( a , " 对应的字符为", chr(a))

# # 最大公约数算法

# # 定义一个函数
# def hcf(x, y):
#    """该函数返回两个数的最大公约数"""

#    # 获取最小值
#    if x > y:
#        smaller = y
#    else:
#        smaller = x

#    for i in range(1,smaller + 1):
#        if((x % i == 0) and (y % i == 0)):
#            hcf = i

#    return hcf


# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))

# print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))

# # 最小公倍数算法

# # 定义函数
# def lcm(x, y):

#    #  获取最大的数
#    if x > y:
#        greater = x
#    else:
#        greater = y

#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1

#    return lcm


# # 获取用户输入
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))

# print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))

# # 简单计算器实现
# # 定义函数
# def add(x, y):
#    """相加"""

#    return x + y

# def subtract(x, y):
#    """相减"""

#    return x - y

# def multiply(x, y):
#    """相乘"""

#    return x * y

# def divide(x, y):
#    """相除"""

#    return x / y

# # 用户输入
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")

# choice = input("输入你的选择(1/2/3/4):")

# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))

# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))

# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))

# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))

# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
# else:
#    print("非法输入")

# # Python 生成日历
# # 引入日历模块
# import calendar

# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))

# # 显示日历
# print(calendar.month(yy,mm))

# # Python 计算每个月天数
# import calendar
# monthRange = calendar.monthrange(2013,7)
# print(monthRange)

# # 获取昨天日期
# # 引入 datetime 模块
# import datetime
# def getYesterday(): 
# 	today=datetime.date.today() 
# 	oneday=datetime.timedelta(days=1) 
# 	yesterday=today-oneday  
# 	return yesterday

# # 输出
# print(getYesterday())

# # 使用递归的方式来生成斐波那契数列
# def recur_fibo(n):
#    """递归函数
#    输出斐波那契数列"""
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))


# # 获取用户输入
# nterms = int(input("您要输出几项? "))

# # 检查输入的数字是否正确
# if nterms <= 0:
#    print("输入正数")
# else:
#    print("斐波那契数列:")
#    for i in range(nterms):
#        print(recur_fibo(i))


# # Python基本的文件操作，包括 open，read，write
# # 写文件
# with open("test.txt", "wt") as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
 
# # Read a file
# with open("test.txt", "rt") as in_file:
#     text = in_file.read()
 
# print(text)

# # Python字符串的判断
# # 测试实例一
# print("测试实例一")
# str = "w3cschool.cn"
# print(str.isalnum()) # 判断所有字符都是数字或者字母
# print(str.isalpha()) # 判断所有字符都是字母
# print(str.isdigit()) # 判断所有字符都是数字
# print(str.islower()) # 判断所有字符都是小写
# print(str.isupper()) # 判断所有字符都是大写
# print(str.istitle()) # 判断所有单词都是首字母大写，像标题
# print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

# print("------------------------")

# # 测试实例二
# print("测试实例二")
# str = "w3cschool"
# print(str.isalnum()) 
# print(str.isalpha()) 
# print(str.isdigit()) 
# print(str.islower()) 
# print(str.isupper()) 
# print(str.istitle()) 
# print(str.isspace()) 

# # Python 字符串大小写转换
# str = "www.w3cschool.cn"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

# #list 常用操作
# li = ["a", "b", "mpilgrim", "z", "example"]
# print(li)
# print(li[1])
# print(li[-1])
# print(li[1:4])
# li.append("new")
# print(li)
# li.insert(2, "new")
# print(li)
# li.extend(["two", "elements"]) 
# print(li)
# li.index("exameple")
# li.remove("z") 
# li.remove("c")     #list 中没有找到值, Python 会引发一个异常
# li.pop()      # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。

# li = ['a', 'b', 'mpilgrim']
# li = li + ['example', 'new']
# 使用join链接list成为字符串
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

# join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
print(["%s=%s" % (k, v) for k, v in params.items()])
print( ";".join(["%s=%s" % (k, v) for k, v in params.items()]))

# 分割字符串
# split 与 join 正好相反, 它将一个字符串分割成多元素 list。
# 注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
# split 接受一个可选的第二个参数, 它是要分割的次数。
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
s.split(";")
s.split(";", 1) 


# list 的映射解析
li = [1, 9, 8, 4] 
[elem*2 for elem in li]  

# dictionary中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params.keys()
params.values()
params.items()
[k for k, v in params.items()]
[v for k, v in params.items()]
["%s=%s" % (k, v) for k, v in params.items()]

# list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]