def printhead(headstring):
    print("**************************************************************************************************************")
    print(printString.center(96,'*'))
    print("**************************************************************************************************************")

# 1.1.如何在列表中根据条件筛选数据
printString = '1.1.如何在列表中根据条件筛选数据'
printhead(printString)

data = [-1, 2, 3, -4, 5]

#筛选出data列表中大于等于零的数据
#第一种方法，不推荐
res1 = []
for x in data:
    if x >= 0:
        res1.append(x)

print(res1)

#第二种用列表解析，推荐使用
res2 = [ x for x in data if x >= 0]
print(res2)

#第三种用filter函数
res3 = list(filter(lambda x : x>= 0,data))
print(res3)

# 1.2.如何在字典中根据条件筛选数据
# print("**************************************************************************************************************")
printString = '1.2.如何在字典中根据条件筛选数据'
printhead(printString)

from random import randint

#创建学生字典,学号为1~20，分数为50~100随机
d = {'student%d'% i: randint(50,100) for i in range(1,21)}
print(d)

#过滤出分数为90的学生字典
#第一种方法
d1 = {k:v for k,v in d.items() if v >= 90}
print(d1)

#第二种方法
d2 = dict(filter(lambda item:item[1] >= 90, d.items()))
print(d2)

# 1.3.如何在集合中根据条件筛选数据
printString = '1.3.如何在集合中根据条件筛选数据'
printhead(printString)
from random import randint

s = {randint(0,20) for _ in range(20)}
print(s)

#筛选出能被3整除的数
s1 = {x for x in s if x % 3 == 0}
print(s1)

# 1.4.如何为元祖中的每个元素命名，提高程序可读性
printString = '1.4.如何为元祖中的每个元素命名，提高程序可读性'
printhead(printString)

# 如下元祖，通过函数判断年龄和性别，但是这样代码可读性很差，别人并不知道student[1],student[2]代表什么意思。如何解决呢
def func(student):
    if student[1] < 18 :
        pass

    if student[2] == 'male':
        pass

student = ('derek',22,'male','111@qq.com')

func(student)

# 方案一：定义枚举类型
#1.4..如何为元祖中的每个元素命名，提高程序可读性

def func(student):
    if student[1] < 18 :
        pass

    if student[2] == 'male':
        pass

s1 = ('derek',22,'male','111@qq.com')

#第一种：使用枚举
from enum import IntEnum

class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

print(s1[StudentEnum.NAME])
print(s1[StudentEnum.AGE])

#第二种：使用标准库中collections.namedtuple替代内置tuple
from collections import namedtuple

Student = namedtuple('student',['name','age','sex','email'])
s2 = Student('derek',22,'male','222@qq.com')
print(s2[0])               #derek
# 可以通过s2.name获取姓名
print(s2.name)             #derek

# 1.5.如何根据字典中值的大小，对字典中的项进行排序
printString = '1.5.如何根据字典中值的大小，对字典中的项进行排序'
printhead(printString)

from random import randint

d = {k: randint(60, 100) for k in 'abcdefg'}
print(d)
#第一种方法：使用列表解析或者zip()函数,把字典的keys和values反转过来
list1 = [(v,k) for k,v in d.items()]
#或者使用zip()函数
# list2 = list(zip(d.values(),d.keys()))
print(list1)
list1 = sorted(list1,reverse=True)
print(list1)

#第二种方法：使用sorted排序
p = sorted(d.items(),key=lambda item:item[1],reverse=True)
print(p)     #[('a', 97), ('b', 93), ('d', 93), ('e', 92), ('f', 76), ('c', 66), ('g', 61)]

#对分数添加一个排名
d = {k:(i,v) for i, (k,v) in enumerate(p,1)}
print(d)    #{'g': (1, 97), 'd': (2, 92), 'f': (3, 91), 'c': (4, 79), 'a': (5, 78), 'e': (6, 67), 'b': (7, 64)}

# 1.6如何统计序列中元素的频度
printString = '1.6如何统计序列中元素的频度'
printhead(printString)
from random import randint
from collections import Counter

data = [randint(1,5) for _ in range(1,20)]
print(data)   #[5, 2, 1, 2, 5, 3, 1, 1, 1, 4, 2, 5, 3, 2, 3, 5, 1, 2, 5]

#计算频度最高的是三个数
c = Counter(data)
print(c.most_common(3))    #[(1, 5), (3, 4), (2, 4)]


# 1.7.如何快速找到多个字典中的公共键
printString = '1.7.如何快速找到多个字典中的公共键'
printhead(printString)
from random import randint,sample
from functools import reduce

d1 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
d2 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
d3 = {k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}

#1.使用字典的keys()方法，得到一个字典keys的集合
#2.使用map函数，得到每个字典keys的集合
#3.使用reduce，取所有字典keys集合的交集

dl = [d1,d2,d3]
#找到三个字典中相同的keys
result = reduce(lambda a,b: a & b, map(dict.keys, dl))
print(result)

# 1.8.如何让字典保持有序
printString = '1.8.如何让字典保持有序'
printhead(printString)
from collections import OrderedDict
from itertools import islice

d = OrderedDict()
d['e'] = 5
d['d'] = 4
d['c'] = 3
d['b'] = 2
d['a'] = 1

print(d)    #OrderedDict([('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)])

#OrderedDict字典，在迭代操作时，它会保持元素被插入时的顺序

def query_by_order(d, a, b =None):
    if b is None:
        b = a + 1
    return list(islice(d,a,b))

#第五个key
res1 = query_by_order(d,4)
print(res1)     #['a']

#第二个和第三个key
res2 = query_by_order(d,1,3)
print(res2)     #['d', 'c']


# 1.9.如何实现用户的历史记录功能
# 使用容量为n的队列存储历史记录

# 使用deque双端循环队列存储历史记录（deque是保存到内存中，下次启动历史记录会消失）
# 如果想保存到硬盘中，使用pickle模块，以便下次启动使用
# 1.9如何实现用户的历史记录功能

from random import randint
from collections import deque
import pickle


def guess(n, k):
    if n == k:
        print('猜对了，这个数字是%d' % k)
        return True
    if n < k:
        print('猜大了，比%d小' % k)
    elif n > k:
        print('猜小了，比%d大' % k)
    return False


def main():
    n = randint(1, 100)
    i = 1
    hq = deque([], 5)
    while True:
        line = input('[%d]请输入一个数字：' % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n, k):
                break
        elif line == 'quit':
            break
        elif line == 'history':
            print(hq)


if __name__ == '__main__':
    main()

# #结果
# [1]请输入一个数字：1
# 猜小了，比1大
# [2]请输入一个数字：2
# 猜小了，比2大
# [3]请输入一个数字：3
# 猜小了，比3大
# [4]请输入一个数字：history
# deque([1, 2, 3], maxlen=5)
# [4]请输入一个数字：