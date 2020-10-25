"""猜数游戏   100以内的随机整数"""
import random                         #导入random库

num = random.randint(0, 100)          #产生0到100内的随机整数
minNum = 0                              #最小随机数
maxNum = 100                            #最大随机数
print('这是一个猜数游戏，你可以输入0到100之间的整数')
guess = int(input('请输入一个数字：'))   #输入猜的数

"""判断猜的数与产生的随机数是否一致,不一致时提醒并要求重新输入数字"""
for guess_count in range(1,999999):
    if guess < num:
        minNum = guess
        print("猜小了,当前数字区间为：", minNum, "-", maxNum)
        guess = int(input('请重新输入一个数字：'))
    elif guess > num:
        maxNum = guess
        print("猜大了，当前数字区间为：", minNum, "-", maxNum)
        guess = int(input('请重新输入一个数字：'))
    else:
        print('恭喜你！猜对了!你共猜了' + str(guess_count) + '次。')
        break