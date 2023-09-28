def printhead(headstring):
    print("**************************************************************************************************************")
    print(printString.center(96,'*'))
    print("**************************************************************************************************************")

#3.1.如何实现可迭代对象和迭代器对象
printString = '3.1.如何实现可迭代对象和迭代器对象'
printhead(printString)

# #3.1 如何实现可迭代对象和迭代器对象

# import requests
# from collections.abc import Iterable,Iterator

# class WeatherIterator(Iterator):
#     def __init__(self,cities):
#         self.cities = cities
#         #从列表中迭代一个city，index就+1
#         self.index = 0

#     def __next__(self):
#         #如果所有的城市都迭代完了，就抛出异常
#         if self.index == len(self.cities):
#             raise StopIteration
#         #当前迭代的city
#         city = self.cities[self.index]
#         #迭代完当前city，index就+1
#         self.index += 1
#         return self.get_weather(city)

#     def get_weather(self,city):
#         url = 'http://xxxx/weather_mini?city=' + city
#         r = requests.get(url)
#         #获取当天的天气信息
#         data = r.json()['data']['forecast'][0]
#         #返回城市名字、最高和最低气温
#         return city, data['high'], data['low']


# class WeatherIterable(Iterable):
#     def __init__(self,cities):
#         self.cities = cities

#     def __iter__(self):
#         return WeatherIterator(self.cities)


# def show(w):
#     for x in w:
#         print(x)

# weather = WeatherIterable(['北京','上海','广州','深圳','东莞'])
# show(weather)


#3.2如何使用生成器函数实现可迭代对象
printString = '3.2如何使用生成器函数实现可迭代对象'
printhead(printString)

from collections.abc import Iterable

class PrimeNumbers(Iterable):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a,self.b):
            if self.is_prime(k):
                yield k

    def is_prime(self,k):
        return False if k < 2 else all(map(lambda x : k % x, range(2, k)))

#打印1到30直接的素数
pn = PrimeNumbers(1, 30)
for n in pn:
    print(n)


#3.3.如何进行反向迭代以及如何实现反向迭代
printString = '3.3.如何进行反向迭代以及如何实现反向迭代'
printhead(printString)
class IntRange:
    def __init__(self,a,b,step):
        self.a = a
        self.b = b
        self.step = step

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield t
            t += self.step
    
    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield t
            t -= self.step

fr = IntRange(1, 10, 2)

for x in fr:
    print(x)

print('=' * 30)

#反向迭代
for y in reversed(fr):
    print(y)