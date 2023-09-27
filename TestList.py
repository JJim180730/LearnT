# 列表
#创建

fruit = ['apple','pear','grape','orange']   

#切片
print(fruit[1])      #pear
print(fruit[1:3])    #['pear', 'grape']
print(fruit[-1])     #orange
print(fruit[:2])     #['apple', 'pear']

# 追加
fruit.append('peach')
print(fruit)         #['apple', 'pear', 'grape', 'orange', 'peach']

# 删除
fruit.remove('peach')   #删除指定的
print(fruit)         #['apple', 'pear', 'grape', 'orange']

fruit.pop()          #删除列表最后一个元素
print(fruit)         #['apple', 'pear', 'grape']

del fruit[2]         #删除指定的索引
print(fruit)         #['apple', 'pear']

# 插入
fruit.insert(1,'grape')   #把‘grape’加入到索引为1的位置
print(fruit)         #['apple', 'grape', 'pear']

# 修改
fruit[2] = 'orange'  #直接修改
print(fruit)         #['apple', 'grape', 'orange']

# 扩展
fruit1 = ['apple','orange']
fruit2 = ['pear','grape']
fruit1.extend(fruit2)
print(fruit1)         #['apple', 'orange', 'pear', 'grape']

# 统计
print(fruit1.count('apple'))    #1

# 排序
fruit1.sort()
print(fruit1)     #['apple', 'grape', 'orange', 'pear']

fruit1.reverse()
print(fruit1)     #['pear', 'orange', 'grape', 'apple']

# 获取下标
print(fruit1.index('apple'))    #3

# 同时获取下标和值
for index,item in enumerate(fruit1):
    print(index,item)
    
# # 结果    
# 0 pear
# 1 orange
# 2 grape
# 3 apple


# 元组
# 创建元组
fruit = ('apple','orange','grape')

# 常用功能
print(fruit.count('apple'))   #1
print(fruit.index('orange'))  #1





# 字典
# 创建
fruit = {1:'apple',2:'orange',3:'grape'}
print(fruit)

# 增加
fruit[4] = 'pear'
print(fruit)      #{1: 'apple', 2: 'orange', 3: 'grape', 4: 'pear'}

# 修改
fruit[4] = 'peach'
print(fruit)      #{1: 'apple', 2: 'orange', 3: 'grape', 4: 'pear'}

# 删除
fruit.pop(4)       #删除指定的key
print(fruit)       #{1: 'apple', 2: 'orange', 3: 'grape'}

# 查找value
print(fruit.get(1))     #apple

fruit = {1:'apple',2:'orange',3:'grape'}

# 循环
for k,v in fruit.items():
    print(k,v)

# 1 apple
# 2 orange
# 3 grape

for k in fruit.keys():
    print(k)

# 1
# 2
# 3

for v in fruit.values():
    print(v)
    
# apple
# orange
# grape





# 集合
# 创建
fruit = set(['apple','orange','pear'])
print(fruit)         #{'orange', 'pear', 'apple'}

# 添加
fruit.add('grape')   #add只能添加一个
print(fruit)         #{'apple', 'orange', 'pear', 'grape'}

fruit.update(['peach','banana'])    #update添加多个
print(fruit)
{'banana', 'pear', 'apple', 'peach', 'grape', 'orange'}

# 删除
fruit.remove('banana')    #删除指定的
print(fruit)

fruit.pop()    #随机删除
print(fruit)

num1 = set([11,22,33,44])
num2 = set([33,44,55,66])

# 并集
print(num1.union(num2))     #{66, 11, 22, 33, 44, 55}

# 差集
print(num1.difference(num2))    #{11, 22}

# 交集
print(num1.intersection(num2))   #{33, 44}