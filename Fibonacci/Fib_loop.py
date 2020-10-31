# -*- coding: utf-8 -*-
"""
  实现斐波那契数列
  方法四：循环语句
"""
a = 0                   #确定初始值
b = 1
num = []
print("**********请输入要打印的斐波拉契数列项数n的值***********")
n = input("enter:")     #输入想计算的项数n

while b >= 1:
    try:                #设置异常，若输入非正整数退出
        n = int(n)
    except ValueError:
        print("输入错误，请输入正整数")
        exit()
    num.append(b)
    a,b = b,a+b
    if len(num) == n:
        print(num[n-1])
        break