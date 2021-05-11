a = 1
while a < 7:
    if(a % 2 == 0):
        print(a,'是偶数')
    else:
        print(a,'是基数')
    a += 1
else:
    print(a,'大于7了')

# python的三目运算符
b = 4
c = 6
print(b) if b > c else print(c)

# 验证用户登录信息
userName = input('请输入用户名')
passWord = input('请输入密码')
if(userName =='wenxiaoli' and passWord =='123'):
    print('密码验证通过')
else:
    print('密码验证失败')


# 求以下分段函数的结果
"""
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = int(input('x = '))
if x>1:
    y = 3*x -5
elif(x>=-1 and x<=1):
    y = x + 2
else:
    y = 5*x +3

print('当x等于%d时,y等于%d'%(x,y))

# 英制英寸单位与公制厘米进行互换，1英寸 = 2.54厘米
value = float(input('输入value = '))
unit = input('输入要转化的单位unit = ')
if unit == 'in' or unit == '英寸':
    result = value*2.54
    print('%d%s转化为厘米是%.2f' % (value,unit,result))
elif unit == 'cm' or unit == '厘米':
    result = value/2.54
    print('%d%s转化为英寸是%.2f',(value,unit,result))
else:
    print('您输入的单位不对，只能输入英寸和厘米')


# 三角形的面积公式
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if(a + b > c and a + c > b and b + c > a):
    print(f'边长为{a},{b},{c}的三角形的周长为:{a+b+c}')
    p  = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print(f'面积为：{area}')
else:
    print('不能构成一个三角形')


