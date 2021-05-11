# 在一行中写入多个语句，使用;进行分隔
import sys; x = 'Hello Python word!你好'; sys.stdout.write(x + '\n')

# 若要不换行输出则在语句的末尾加上，
print('How to learn python good?')
print('1.Makes English as your working language')
print('2.Practice makes perfect')
print("3.Dont't be one of leeches")
print('2.All experience comes from mistakes')
print('5.Either outstanding or out')

x = 'a'
y = 'b'
print(x)
print(y)

print('------------')
print(x),
print(y)

# python 中的缩进
if True:
    print('true')
else:
    print('false')

# 字符串截取
str = 'Hello python word'
print(str[0:3])
print(str + ' cc')
print(str[0:])

print(str * 2)
if('h' in str):
    print('h 包含在字符串str中')
else:
    print('不包含h')

# r代表不对字符串进行转义
print(r'\n')

# 字符串格式化操作
print('我是%s，我今年%d岁了,该结婚生孩子了，每天学习编程1小时，学习python编程100天' %('文孝礼',31))

# 多行字符串
str = '''
如果我爱你，
绝不像攀援的凌霄花\n
借你的高枝炫耀自己(\t)
'''

print(str)

name = 'f方法可以输出变量方法。'
print(f'{name}')

#字符串的方法
print('123'.center(30,'*'))
print(' 456 '.lstrip())

url = 'www.wenxiaoli.com'
print(url.count('w',0,len(str)))

hello = ('h','e','l','l')
joinHello = ('-').join(hello)
print(('-').join(hello)) # join方法用来将一个字符串进行拼接

splitHello = joinHello.split('-')
print(splitHello)

str = 'this is a String example!'
print(str.replace('is','was',1))
print(str.startswith('this'))
print(str.endswith('le!'))

"""
这里是多行注释，python的多行注释，使用三个""","""
"""

