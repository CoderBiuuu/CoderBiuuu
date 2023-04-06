
# 字符类型
# str
if 0:
    char = 'abc123abc'
    print('字符串:', char)
    # 统计字符串的长度 length
    print("字符串长度", len(char))
    # 查找一个字符串中第一个出现的字符所在的索引（位置）, julia 索引从1开始
    print('1所在的位置：', char.index('1'))
    print('a所在的位置：', char.index('a'))
    # 索引的使用
    print("根据索引查找字符", char[0], char[1], char[-1], char[-2])
    # 替换
    print('替换:', char.replace('123', '456'))
    # 替换所有的a
    print('替换是对所有元素都做替换', char.replace('a', 'x'))
    # 取索引为1和2的字符串，左闭右开
    print("切片", char[1:3])
    # print(list(char))

# list列表
if 0:
    lis1 = ['a', 'b', 'c', '1']
    # 统计列表的长度
    print('长度:', len(lis1))
    # 修改对应索引的元素
    lis1[0] = 'aa'
    print('修改索引为0的元素', lis1)
    # 查找元素为b的索引
    print('b的位置:', lis1.index('b'))
    lis1.append('x')
    print('追加元素x：', lis1)
    # insert，根据素索引追加元素
    lis1.insert(1, 'y1')
    print('insert:', lis1)
    # ['aa', 'y1', 'b', 'c', '1', 'x']
    lis1.insert(-1, 'y-1')
    print(lis1)
    lis1.insert(-2, 'y-2')
    print(lis1)
    # ['aa', 'y1', 'b', 'c', '1', 'y-2', 'y-1', 'x']
    lis1.pop()
    print('删除最后一个元素：', lis1)
    # 排序
    # ['aa', 'y1', 'b', 'c', '1', 'y-2', 'y-1']
    # lis1 = ['+', 'z', 'a', '1']
    # 特殊符号在前，数字在后，字母更后（小写前，大写后）
    # 排序，升序
    lis1.sort()
    print(lis1)
    # ['1', 'aa', 'b', 'c', 'y-1', 'y-2', 'y1']
    # 翻转列表
    # lis1.reverse()
    # print(lis1)
    # ['y1', 'y-2', 'y-1', 'c', 'b', 'aa', '1']
    # 反转的第二种写法
    lis1 = lis1[::-1]
    print(lis1)
    # ['y1', 'y-2', 'y-1', 'c', 'b', 'aa', '1']
    lis1 = ['a', 'b', 'c', '1']
    lis2 = ['x', 'y', 'z', '0'] # > ['a', 'b', 'c', '1', 'x', 'y', 'z', '0']
    lis1.extend(lis2)
    # 合并操作
    print('合并结果:', lis1)
    #
    # print(list(zip(lis1, lis2)))



# dict字典
if 0:
    # 人物信息, person_info
    person_info = dic1 = {'name': 'a', 'age': 18}
    print('键值对', dic1['name'])
    # 修改键值对
    dic1['name'] = '阿凡达'
    print('修改键值对', dic1)
    # 增加键值对
    dic1['gender'] = 'Male'
    print(dic1)
    # 无则新增，有则覆盖
    dic1['gender'] = 'Female'
    print(dic1)
    dic1.update({"gender": 'Bisexual'})
    print(dic1)
    # {'name': '阿凡达', 'age': 18, 'gender': 'Bisexual'}
    # 删除
    dic1.pop('name')
    print('删除', dic1)
    # del dic1['name']
    # print(dic1)
    # 删除本身没有的键值对
    # del dic1['phone']
    # dic1.pop('phone')
    # try:
    #     del dic1['phone']
    # except:
    #     pass
    # print(dic1)

    # {'name': '阿凡达', 'age': 18, 'gender': 'Bisexual'}

    # print('年龄', dic1['age'])
    # print(dic1['address'])

    # 避免报错，同时也能赋予默认值
    print('已有值直接返回', dic1.get('age', '收纳所'))
    print('未有的值则返回默认值', dic1.get('address', '收纳所'))

    dic1 = {'name': 'a', 'age': 18, 'gender': "F"}
    dic2 = {'name': 'b', 'age': 28, 'address': 'China'}
    # dic1.update(dic2)
    # print(dic1)
    dic = dict(dic1, **dic2)
    print('用新的字典更新旧的字典', dic)



# tuple元组
if 0:
    # t1 = [1, 2, 3]
    # t1[1] = 4
    # print(t1)
    t1 = (1, 2, 3)
    # 报错
    t1[1] = 4
    # t1 += (4, )
    # print(t1)



# set集合
if 1:
    s1 = set()
    print(s1)
    # 增加一个元素1
    s1.add(1)
    # 增加一个元素4
    s1.add(4)
    print(s1)
    s2 = {1, 2, 3}
    dic = {'num1': 1, 'num2': 2, 'num3': 3} # 键值对
    print(s2, type(s2))
    print(dic, type(dic))
    # print(s2, type(s2))
    # 交并集
    s1 = {1, 4}
    s2 = {1, 2, 3}
    print('交集', s1 & s2)
    print('并集', s1 | s2)
    # 删除元素
    s1.remove(1)
    print(s1)
    # print(len(s1))
