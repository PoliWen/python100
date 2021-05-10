"""
关于python的变量命名规范：
1.由字母数字和下划线构成，不能使用数字开头
2.区分大小写
3.不能使用保留关键字
4.用小写字母拼写，多个单词用_连接
例如：my_name,first_name,last_name
5.保护变量使用一个_开头
例如：_age;_weight
6.私有变量使用两个__开头
例如：__salary(薪水)
7.命名原则：见名知意
"""

a = 2
b = 3
c = True
d = 'This is a string'
e = 1+5j
f = 3.14152
print(a**b) # **代表求平方运算
print(a/b) # 除法运算
print(a%b) # 取模运算
print(a//b) # 取整数，向下取接近商的整数


# 使用type可以检测变量的数据类型
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#使用int(),float(),str(),chr(),ord()可以进行数据之间的转化
print(ord('A'),ord('a')) # ord()方法将字符串(一个字符)转化成对应的编码(整数)
print(chr(97)) # 将编码(整数)转化为字符串(一个字符)
print(float(3))
print(str(3))
print(int(3.1415926)) #π

#对输入的数字进行计算
a = int(input('a = '))
b = int(input('a = '))
print('%d + %d = %d' % (a,b,a+b))

#写一个华氏度转摄氏度的程序，c = (f-32)/1.8
f = float(input('f = '))
print(f)
def f_to_c(f):
    return (f-32)/1.8
print('华氏度%.2f 转化为摄氏度是 %.2f' %(f,f_to_c(f)))  # %f会强制转化为浮点数,%.1f表示保留一位小数，%.2f表示保留两位小数


#写一个求圆的面积与周长的函数
import math
r = float(input('r = '))
π = math.pi 
print(π)
def cirCle_area(r):
    return π * r * r

#求一个圆的周长
def cirCle_perimeter(r):
    return 2 * π * r

print('周长为%.2f的圆的面积是:%.2f,周长是:%.2f' % (r,cirCle_area(r),cirCle_perimeter(r)))

