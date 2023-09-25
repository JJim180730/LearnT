import os, shutil
import random
os.getcwd()      # 返回当前的工作目录
#os.chdir('/server/accesslogs')   # 修改当前的工作目录
#os.system('mkdir today')   # 执行系统命令 mkdir 

import shutil  #针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
#shutil.copyfile('data.db', 'archive.db')

#shutil.move('/build/executables', 'installdir')

#glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob
glob.glob('*.py')

#通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量
import sys
print(sys.argv)

#sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息
sys.stderr.write('Warning, log file not found starting a new one\n')

#re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')  #简单的功能，应该首先考虑字符串方法

#math 模块为浮点运算提供了对底层 C 函数库的访问:random 提供了生成随机数的工具
import math
math.cos(math.pi / 4)
math.log(1024, 2)
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

#其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:

# from urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#      line = line.decode('utf-8')  # Decoding the binary data to text.
#      if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#          print(line)


# import smtplib
# server = smtplib.SMTP('localhost')
# #server.sendmail()


#datetime 模块为日期和时间处理同时提供了简单和复杂的方法
from datetime import date
#以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib,gzip,zipfile,tarfile

s = b'witch which has which witches wrist watch'
print(len(s))
t1 = zlib.compress(s,5)
t2 = gzip.compress(s,5)

print(len(t1))
print(len(t2))