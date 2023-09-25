# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：

# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'W3CSchool',
    'url' : 'http://www.w3cschool.cn'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码 JSON 数据
# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data1, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)