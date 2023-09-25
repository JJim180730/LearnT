s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


#  repr() 函数可以转义字符串中的特殊字符py
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是 Python 的任何对象
repr((x, y, ('spam', 'eggs')))


for x in range(1, 11):
     print(repr(x).rjust(3), repr(x*x).rjust(4), end=' ')
     # 注意前一行 'end' 的使用
     print(repr(x*x*x).rjust(5))


for x in range(1, 11):
     print('{0:3d} {1:4d} {2:5d}'.format(x, x*x, x*x*x))



"""这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

另一个方法 zfill(), 它会在数字的左边填充 0"""

'12'.zfill(5)

print('We are the {} who say "{}!"'.format('knights', 'Ni'))  #括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。

print('{0} and {1}'.format('spam', 'eggs'))  #在括号中的数字用于指向传入对象在 format() 中的位置

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')) #如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg')) #位置及关键字参数可以任意的结合

#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
