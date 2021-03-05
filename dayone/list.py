# 列表

list = ['red','green','blue']
for c in list:
    print(c)

print(len(list))
list.append('yellow')
print(list)
print('red' in list)
list2 = ['orange','white']
list.extend(list2)
print(list)
list.append(list2)
print(list)
del list[2] # 删除列表中指定的某一个元素
print(list)
list.pop() # 删除最后一个
print(list)
list.reverse()
print(list)
list.insert(2,'blue') # insert方法往元祖里面插入某一项数据
print(list)
list.remove('blue') # 移除某一个元素
print(list)
redIdx = list.index('red')  #查找某一个元素的序号
print(redIdx)

print('''
How to learn python good?
1.Make English as your working language
2.practice makes perfect
3.Don't to be a leeches
4.All experience comes from mistakes
5.Either outstanding or out
''')

print(list(range(10)))