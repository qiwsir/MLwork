# -*- coding: utf-8 -*-
"""
 实现斐波那契数列
  方法一：生成器
"""

def Fib_yield_while(max):   ## 函数名命名不规范
    a, b = 0, 1                #设置初始值
    while max > 0:
        a, b = b, a + b
    max -= 1
    yield a                    #执行yield函数

def Fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):          #循环遍历n次
        a, b = b, a + b
        yield a

if __name__ == "__main__":

    while 1:
        print("**********请输入要打印的斐波拉契数列项数n的值***********")
        n = input("enter:")      #输入要计算的项数n
        if not n.isdigit():      #判断输入值是否为数字
            print("请输入一个正整数！")
            continue
        n = int(n)
        for i in Fib_yield_for(n):
            print(i)
