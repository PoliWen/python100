a = 1
while a < 7:
    if(a%2 == 0):
        print(a,'是偶数')
    else:
        print(a,'是基数')
    a+=1
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


