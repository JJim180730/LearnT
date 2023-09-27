city = ['beijing','shanghai','tinajin','chongqin']
it = iter(city)
print(type(it))
#方法一：使用next方法来使用迭代器
print(it.__next__())
print(it.__next__())

# 方法二：使用for循环来使用迭代器
it.__init__
for x in it:
    print(x)



def generator(low,high):
    while low <= high:
        yield low
        low += 1
for i in generator(1,10):
    print(i,end=' ')


def generator(start = 0):
    while True:
        yield start
        start += 1
for number in generator(4):
    print(number,end=' ')
    if number > 20:
        break

a = [i*2 for i in range(1,10)]
print(a)