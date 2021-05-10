#输入一个年份判断是不是闰年，闰年的定义：4年一润100年不闰，400年再润
#计算规则：1.能被4整除，且不能被100整除 2.能被400整除
year = int(input('year = '))
def is_leap(y):
    return (y%4==0 and y%100!=0) or y%400 == 0
    
print('%d是闰年' %(year)) if is_leap(year) else print('%d不是闰年' %(year))
