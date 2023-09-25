#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能

print('orange' in basket)                 # 快速判断元素是否在集合内
print('crabgrass' in basket)


a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a-b)

print(a|b)

print(a&b)

print(a^b)

thisset = set(("Google", "W3Cschool", "Taobao"))
thisset.add("Baidu")
print(thisset)

thisset = set(("Google", "w3Cschool", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)

hisset = set(("Google", "W3Cschool", "Taobao"))
thisset.remove("Taobao")
print(thisset)

#thisset.remove("Facebook")   # 不存在会发生错误

thisset = set(("Google", "W3Cschool", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

thisset = set(("Google", "W3Cschool", "Taobao", "Facebook"))
x = thisset.pop()

print(x)
print(thisset)

thisset = set(("Google", "W3cschool", "Taobao"))
thisset.clear()
print(thisset)