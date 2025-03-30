# 定义一个包含不同类型元素的列表
my_list = [1, 'Python', 3.14, True]

# 访问列表中的元素（索引从0开始）
print(my_list[0])  # 输出: 1
print(my_list[1])  # 输出: Python

# 修改列表中的元素
my_list[2] = 2.71
print(my_list)  # 输出: [1, 'Python', 2.71, True]

# 添加元素到列表末尾
my_list.append('添加的元素')
print(my_list)  # 输出: [1, 'Python', 2.71, True, '添加的元素']

# 插入元素到指定位置
my_list.insert(1, '插入的元素')
print(my_list)  # 输出: [1, '插入的元素', 'Python', 2.71, True, '添加的元素']

# 删除列表中的元素
del my_list[0]
print(my_list)  # 输出: ['插入的元素', 'Python', 2.71, True, '添加的元素']

# 使用remove方法删除指定值的元素
my_list.remove('Python')
print(my_list)  # 输出: ['插入的元素', 2.71, True, '添加的元素']

# 列表切片
print(my_list[1:3])  # 输出: [2.71, True]

# 列表长度
print(len(my_list))  # 输出: 4

# 列表遍历
for item in my_list:
    print(item)