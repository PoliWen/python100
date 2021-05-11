# while循环猜数字
import random

result = random.randint(1,100)
count = 0
while True:
    guess = int(input('请输入你猜的数字'))
    count += 1
    if(guess > result):
        print('你猜大了')
    elif(guess < result):
        print('你猜小了')
    else:
        print('恭喜你猜对了')
        break

print(f'你总共猜了，{count}次')

if(count > 7):
    print('你的智商余额明显不足，需要充值了')